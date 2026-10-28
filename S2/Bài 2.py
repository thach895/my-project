def classify_logistics_feature(feature_name):
    feature = feature_name.lower()

    # Nhóm từ khóa TPS
    tps_keywords = [
        "đã lấy hàng",
        "lấy hàng",
        "quét mã",
        "mã vạch",
        "in phiếu",
        "phiếu cước",
        "thanh toán",
        "cập nhật trạng thái"
    ]

    # Nhóm từ khóa MIS
    mis_keywords = [
        "báo cáo",
        "thống kê",
        "doanh thu tháng",
        "doanh thu",
        "tuần",
        "tháng"
    ]

    # Nhóm từ khóa DSS
    dss_keywords = [
        "dự báo",
        "phân tích",
        "điểm nóng",
        "quá tải",
        "mở thêm",
        "chiến lược",
        "3 năm",
        "3 tháng"
    ]

    # Kiểm tra DSS trước để tránh nhầm với báo cáo
    if any(keyword in feature for keyword in dss_keywords):
        return "DSS"

    if any(keyword in feature for keyword in mis_keywords):
        return "MIS"

    if any(keyword in feature for keyword in tps_keywords):
        return "TPS"

    return "Không xác định"


# Dữ liệu kiểm thử
features = [
    "Báo cáo tổng hợp doanh thu tháng",
    "Tài xế bấm nút Đã lấy hàng",
    "Nhân viên kho quét mã vạch nhập kho",
    "In phiếu cước giao hàng",
    "Dự báo điểm nóng quá tải đơn hàng mùa Tết"
]

for feature in features:
    print(f"{feature} --> {classify_logistics_feature(feature)}")