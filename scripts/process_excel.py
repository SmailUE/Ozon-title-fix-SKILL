from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
import io

# Excel全局美化配置（无隔行斑马颜色）
def set_table_style(ws):
    # 表头样式
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    left_align = Alignment(horizontal="left", vertical="top", wrap_text=True)

    # 写入表头文本
    ws["A1"] = "Исходное название"
    ws["B1"] = "Стандартный заголовок"
    ws["C1"] = "Рекламный заголовок"

    # 表头统一格式
    for col in ["A", "B", "C"]:
        cell = ws[f"{col}1"]
        cell.font = header_font
        cell.fill = header_fill
        cell.border = thin_border
        cell.alignment = center_align

    # 固定列宽
    ws.column_dimensions["A"].width = 50
    ws.column_dimensions["B"].width = 45
    ws.column_dimensions["C"].width = 65
    ws.freeze_panes = "A2"

    # 内容行统一边框+左对齐
    max_row = ws.max_row
    for row in range(2, max_row + 1):
        for col in range(1, 4):
            cell = ws.cell(row=row, column=col)
            cell.border = thin_border
            cell.alignment = left_align

# 读取Excel第一列所有原始标题
def read_source_excel(file_bytes: bytes) -> list:
    stream = io.BytesIO(file_bytes)
    wb = load_workbook(stream)
    sheet = wb["Sheet1"]
    title_list = []
    for r in range(1, sheet.max_row + 1):
        val = sheet.cell(row=r, column=1).value
        title_list.append(str(val) if val is not None else "")
    return title_list

# 生成优化后完整Excel二进制文件
def generate_output_excel(origin_titles: list, std_titles: list, promo_titles: list) -> bytes:
    wb = Workbook()
    ws = wb.active
    ws.title = "Оптимизированные заголовки"
    # 批量写入数据
    total = len(origin_titles)
    for idx in range(total):
        row_num = idx + 2
        ws.cell(row=row_num, column=1, value=origin_titles[idx])
        ws.cell(row=row_num, column=2, value=std_titles[idx])
        ws.cell(row=row_num, column=3, value=promo_titles[idx])
    # 应用美化格式
    set_table_style(ws)
    # 导出字节流
    output_buffer = io.BytesIO()
    wb.save(output_buffer)
    output_buffer.seek(0)
    return output_buffer.getvalue()


if __name__ == "__main__":
    print("russian-title-optimizer Excel processor loaded")
    print("Usage: read_source_excel() load raw file, generate_output_excel() export formatted xlsx")