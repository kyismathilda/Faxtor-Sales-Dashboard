import streamlit as st
import pandas as pd

# CONFIG

st.set_page_config(layout="wide")


# CUSTOM CSS

st.markdown("""
<style>

/* Background */
.main {
    background-color: #f7f8fc;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #eef1fb;
    padding: 20px;
}

/* Sidebar menu */
div[role="radiogroup"] > label {
    background-color: #dbe2ff;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 500;
}

div[role="radiogroup"] > label:hover {
    background-color: #cfd7ff;
}

/* Metric card */
div[data-testid="metric-container"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* Progress bar */
.stProgress > div > div > div > div {
    background-color: #ff4b5c;
}

/* Title */
h1, h2, h3 {
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR

with st.sidebar:
    st.image("logo_faxtor.png", width=1000)
    st.markdown("## Business Dashboard")

    page = st.radio(
        "Features",
        [
            "Revenue & Profit Tracker",
            "Monthly Business Performance",
            "New Client Tracker",
            "Expansion Tracker",
            "Faxtor 2026 Calendar",
            "Royalty Calculator",
            "Sales Forecaster"
        ]
    )


# INPUT DATA

royalty_pricing = {
    "PII": 45000,
    "OPTI": 40000,
    "MSSQ": 40000,
    "GWS": 45000,
    "INCRITS": 50000,
}

revenue_actual=4444517542
revenue_target=9000000000
profit_actual=1108540232
profit_target=3600000000

expansion_data = {
    "Jawa":{"Banten":54,"DIY":16,"DKI Jakarta":168,"Jawa Barat":232,"Jawa Tengah":23,"Jawa Timur":32},
    "Sumatra":{"Aceh":7,"Bangka Belitung":2,"Jambi":2,"Kep. Riau":5,"Lampung":4,"Riau":4,"Sumatra Barat":7,"Sumatra Selatan":3,"Sumatra Utara":23},
    "Kalimantan":{"Kalimantan Barat":3,"Kalimantan Selatan":1,"Kalimantan Tengah":4,"Kalimantan Timur":8,"Kalimantan Utara":2},
    "Sulawesi":{"Sulawesi Tenggara":4,"Sulawesi Selatan":6},
    "BaliNusra":{"Bali":8,"NTB":2, "Lombok":1},
    "Papua":{"Jayapura":2,"Sorong":1},
}

image_map = {
    "Jawa":"Jawa.png",
    "Sumatra":"Sumatra.png",
    "Kalimantan":"Kalimantan.png",
    "Sulawesi":"Sulawesi.png",
    "BaliNusra":"Bali.png",
    "Papua":"Papua.png",
}

standard_pricing= {
    "BIG FIVE": 30000,"EII": 40000,"FCAT": 90000,"FCAT Short": 50000,"FEAST": 40000,
    "FMAT": 50000,"FTPI": 30000,"GWS": 45000,"IAMAR": 40000,"INCRITS": 50000,
    "LSSI": 20000,"MSSQ MSDQ": 40000,"OPTI": 50000,"PII": 45000,
    "Package 1 - Student Ultimate Assessment": 195000,
    "Package 2 - Complete Critical Thinking Assessment (OPTI Vers)": 215000,
    "Package 3 - Complete Critical Thinking Assessment": 190000,
    "Package 4 - High School Majoring Assessment": 175000,
    "Package 5 - Corporate Complete Assessment": 160000,
    "Package 6 - Career Mapping Assessment": 130000,
    "Package 7 - Corporate Complete Assessment Short Vers": 110000,
    "Package 8 - Middle School Selection Assessment": 95000,
    "Package 9 - Corporate Brief Assessment": 80000,
    "Package 10 - Middle School Selection Assessment Short Vers": 60000,
}

professional_pricing= {
    "BIG FIVE": 35000,"EII": 45000,"FCAT": 100000,"FCAT Short": 60000,"FEAST": 45000,
    "FMAT": 60000,"FTPI": 35000,"GWS": 50000,"IAMAR": 50000,"INCRITS": 55000,
    "LSSI": 25000,"MSSQ MSDQ": 45000,"OPTI": 60000,"PII": 50000,
    "Package 1 - Student Ultimate Assessment": 230000,
    "Package 2 - Complete Critical Thinking Assessment (OPTI Vers)": 250000,
    "Package 3 - Complete Critical Thinking Assessment": 220000,
    "Package 4 - High School Majoring Assessment": 205000,
    "Package 5 - Corporate Complete Assessment": 175000,
    "Package 6 - Career Mapping Assessment": 155000,
    "Package 7 - Corporate Complete Assessment Short Vers": 140000,
    "Package 8 - Middle School Selection Assessment": 110000,
    "Package 9 - Corporate Brief Assessment": 90000,
    "Package 10 - Middle School Selection Assessment Short Vers": 70000,
}

gross_target=750000000

logo_map = {
    "BIG FIVE": "BIGFIVE.png",
    "EII": "EII.png",
    "FCAT": "FCAT.png",
    "FCAT Short": "FCATS.png",
    "FEAST": "FEAST.png",
    "FMAT": "FMAT.png",
    "FTPI": "FTPI.png",
    "GWS": "GWS.png",
    "IAMAR": "IAMAR.png",
    "INCRITS": "INCRITS.png",
    "LSSI": "LSSI.png",
    "MSSQ MSDQ": "MSSQ.png",
    "OPTI": "OPTI.png",
    "PII": "PII.png",
}

# PAGE 1

if page == "Revenue & Profit Tracker":

    revenue_pct = (revenue_actual/revenue_target)*100
    profit_pct = (profit_actual/profit_target)*100

    st.title("Business Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue")
        st.metric("", f"Rp{revenue_actual:,}", f"{revenue_pct:.0f}% of target")

    with col2:
        st.subheader("Profit")
        st.metric("", f"Rp{profit_actual:,}", f"{profit_pct:.0f}% of target")

    st.subheader("Progress to Target")

    st.progress(revenue_pct/100)
    st.caption(f"{revenue_pct:.0f}%")

    st.progress(profit_pct/100)
    st.caption(f"{profit_pct:.0f}%")


# PAGE 2
elif page == "Monthly Business Performance":

    import matplotlib.pyplot as plt

    st.title("Monthly Business Performance")

    data = {
        "January": {
            "gross": 104,
            "gross_nominal": "Rp780.201.044",
            "gross_insight": "We successfully surpassed the Gross Target by 104% (Rp780.201.044).",

            "nett": 85,
            "nett_nominal": "Rp254.435.608",
            "nett_insight": "Though we achieved Gross Target, minimum Nett Income is Rp300.000.000 / month, yet we have -15% shortfall due to high operational cost.",

            "growth_lm": 24,
            "growth_lm_text": "vs Gross LM Dec’25 (Rp631.020.560)",

            "growth_ytd": 250,
            "growth_ytd_text": "vs Gross YTD Jan’25 (Rp295.485.500)",

            "client": 17,
            "client_text": [
                "PT. Tilaka Nusa Teknologi - Jakarta",
                "Paddy Indonesia - Bandung",
                "Yayasan Wakaf Nurul Iman - Jakarta",
                "Biro Catharsis - Bandung",
                "PP Fitri Andriyani - Bandung",
                "PT. Dimiha Kolaborasi Sukses - ",
                "Integrita Global Sertifikat - Tangerang",
                "Biro Waskita - Solo",
                "Biro Optimal - Palembang",
                "Biro Widya Talenta - Padang",
                "LPT Dewantara - Yogyakarta",
                "Biro Wharna Bhumi Academy - Bali",
                "Biro Al Chair Consulting - Aceh",
                "LPK Nobori Seiko Indonesia - Bekasi",
                "PP Maria Angelisa Siregar - Banyumas",
                "PP Nadia Ayu Safira - Bandung",
                "PP Adri Kurniawan - Jakarta",
                "Yayasan Himma Aliya - Bogor",
            ],

            "tools": {
                "FCAT": 581, "FCATs": 1171, "FCAT-R": 27, "FTPI": 1107,
                "BIG FIVE": 524, "FEAST": 3403, "LSSI": 262, "IAMAR": 48,
                "PII": 98, "EII": 138, "INCRITS": 45, "OPTI": 117,
                "MSSQ": 27, "MSDQ": 28, "GWS": 3
            }
        },

        "February": {
            "gross": 133,
            "gross_nominal": "Rp1.001.571.243",
            "gross_insight": "We successfully surpass the Gross Target by 133% (Rp1.001.571.243).",

            "nett": 60,
            "nett_nominal": "Rp179.777.293",
            "nett_insight": "Though we achieved Gross Target, minimum Nett Income is Rp300.000.000 / month, yet we have -34% shortfall due to high operational cost (Kimia Farma Project).",

            "growth_lm": 29,
            "growth_lm_text": "vs Gross LM Jan’26 (Rp780.201.044)",

            "growth_ytd": 238,
            "growth_ytd_text": "vs Gross YTD Feb’25 (Rp421.875.500)",

            "client": 7,
            "client_text": [
                "PT Quadra Sinergi Consulting - Balikpapan",
                "PP Habi Maulana - Sorong, Papua",
                "PP Fredy Andri - Bandung",
                "Bianglala Nanda - Bandung",
                "PP Trifiana Tiodora - Jakarta",
                "PP Juliana - Medan",
                "PP Belladiena Azmi - Mojokerto",
            ],
            "tools": {
                "FCAT": 3305, "FCATs": 1755, "FCAT-R": 45, "FTPI": 1778,
                "BIG FIVE": 989, "FEAST": 5285, "LSSI": 134, "IAMAR": 36,
                "PII": 918, "EII": 64, "INCRITS": 2364, "OPTI": 2888,
                "MSSQ": 239, "MSDQ": 232, "GWS": 7
            }
        },

        "March": {
            "gross": 88,
            "gross_nominal": "Rp659.070.130",
            "gross_insight": "We partially surpass the Gross Target by 88% (Rp659.070.130).",

            "nett": 107,
            "nett_nominal": "Rp321.413.421",
            "nett_insight": "We successfully achieved minimum Nett Income in March",

            "growth_lm": -34,
            "growth_lm_text": "vs Gross LM Feb’26 (Rp1.001.103.500)",

            "growth_ytd": 87,
            "growth_ytd_text": "vs Gross YTD Mar’25 (Rp351.598.000)",

            "client": 7,
            "client_text": [
                "PP Dwi Bektiningsih - Bandung",
                "PP Yoas Pasali - Bandung",
                "Biro Psikologi Schema - Depok",
                "PT. Astari Niagara (Acrylic Factory) - Tangerang",
                "PP Siti Ulfa Hutabarat - Medan",
                "Thoriq Imamul Asykar - Jakarta",
                "LPK Amanat Negeri Sakura - Cianjur",
            ],
            "tools": {
                "FCAT": 540, "FCATs": 610, "FCAT-R": 538, "FTPI": 1095,
                "BIG FIVE": 939, "FEAST": 19357, "LSSI": 34, "IAMAR": 18,
                "PII": 28, "EII": 35, "INCRITS": 261, "OPTI": 347,
                "MSSQ": 37, "MSDQ": 24, "GWS": 1
            }
        },
    
        "April": {
            "gross": 128,
            "gross_nominal": "Rp961.506.500",
            "gross_insight": "We successfully surpass the Gross Target by 128% (Rp961.506.500).",

            "nett": 118,
            "nett_nominal": "Rp352.913.910",
            "nett_insight": "We successfully achieved minimum Nett Income in April.",

            "growth_lm": 46,
            "growth_lm_text": "vs Gross LM Mar’26 (Rp659.070.130)",

            "growth_ytd":921,
            "growth_ytd_text": "vs Gross YTD Apr’25 (Rp104.356.500)",

            "client": 21,
            "client_text": [
                "Yayasan Daarut Tauhid (LAZ) - Bandung",
                "PP Yudithh Bernadette - Bogor",
                "PP Reny Rachmawatie - Jakarta",
                "Klinik D'Fun Station - Bandung",
                "PP Disa Nisrina Listiani - Tangerang",
                "PP Dina Islamiyah - Bandung",
                "PT. Mitra Cakrawala International Group - Jakarta",
                "PP Yanti Mujiharti - Jakarta",
                "PP Bhumidana Indonesia - Bandung",
                "PP Ninette Putri Mustika - Jakarta",
                "Layanan Sedari Diri - Tangerang",
                "Biro Human Persona - Jakarta",
                "PP Devita - Jakarta",
                "PLP Universitas Hasanuddin - Sulawesi Selatan",
                "Suhu Training - Yogyakarta",
                "Five Psychology - Yogyakarta",
                "Kelompok Riset Leadership UI - Depok",
                "Yayasan Cahaya Mutiara / Sekolah Mutiara Bunda - Bandung",
                "Biro Bina Citra - Yogyakarta",
                "Klinik Mayapada - Jakarta",
                "PP Fairuz Syifa Rosyidah - Jakarta",
                
            ],
            "tools": {
                "FCAT": 4393, "FCATs": 4035, "FCAT-R": 513, "FTPI": 3345,
                "BIG FIVE": 2707, "FEAST": 9590, "LSSI": 389, "IAMAR": 84,
                "PII": 261, "EII": 125, "INCRITS": 2421, "OPTI": 2819,
                "MSSQ": 320, "MSDQ": 308, "GWS": 3
            }
        },
        "May": {
            "gross": 55,
            "gross_nominal": "Rp414.328.550",
            "gross_insight": "We partially surpass the Gross Target by 55% (Rp414.328.550).",

            "nett": 1.5,
            "nett_nominal": "Rp4.502.782",
            "nett_insight": "We haven't achieved minimum Nett Income in May.",

            "growth_lm": -57,
            "growth_lm_text": "vs Gross LM Apr’26 (Rp961.506.500)",

            "growth_ytd":-2,
            "growth_ytd_text": "vs Gross YTD May’25 (Rp424.011.350)",

            "client": 8,
            "client_text": [
                "Arutala Growth Corner - Kab. Lombok Barat",
                "PP Susilawati - Tangerang",
                "KOBI Education - Bandung",
                "Katamistry Consulting - Jakarta Selatan",
                "Bunayya Counselor - Depok",
                "Fresnel Pialang Asuransi Mandiri - Jakarta Selatan",
                "Humanis Psikologi - Tangerang Selatan",
                "Fakultas Hukum UGM - Yogyakarta",
            ],
            "tools": {
                "FCAT": 575, "FCATs": 1739, "FCAT-R": 220, "FTPI": 2451,
                "BIG FIVE": 991, "FEAST": 6360, "LSSI": 100, "IAMAR": 215,
                "PII": 124, "EII": 132, "INCRITS": 140, "OPTI": 499,
                "MSSQ": 298, "MSDQ": 288, "GWS": 6
            }
        },
    }
    month = st.radio("Choose Month", list(data.keys()), horizontal=True)
    d = data[month]

   
    def donut(value):
        fig, ax = plt.subplots()

        # FIX supaya tidak negatif
        display_value = min(value, 100)

        ax.pie(
            [display_value, 100 - display_value],
            colors=["#4aa3c7", "#e5e7eb"],
            startangle=90,
            counterclock=False,
            wedgeprops={'width': 0.3}
        )

        ax.text(0, 0, f"{value}%", ha='center', va='center', fontsize=18, fontweight='bold')

        return fig

   
    col1, col2, col3 = st.columns([2,2,1])

   
    with col1:
        st.subheader("GROSS TARGET")
        st.pyplot(donut(d["gross"]))
        st.markdown(f"**{d['gross_nominal']}**")
        st.caption(d["gross_insight"])

   
    with col2:
        st.subheader("NETT TARGET")
        st.pyplot(donut(d["nett"]))
        st.markdown(f"**{d['nett_nominal']}**")
        st.caption(d["nett_insight"])

    
    with col3:
        st.subheader("Growth")

        icon_lm = "arrow_up.png" if d["growth_lm"] >= 0 else "arrow_down.png"
        icon_ytd = "arrow_up.png" if d["growth_ytd"] >= 0 else "arrow_down.png"

        st.image(icon_lm, width=100)
        st.metric("vs Last Month", f"{d['growth_lm']}%")
        st.caption(d["growth_lm_text"])

        st.image(icon_ytd, width=100)
        st.metric("vs YTD", f"{d['growth_ytd']}%")
        st.caption(d["growth_ytd_text"])

   
    st.subheader("New Client")
    st.markdown(f"## {d['client']}")

    # bullet point client
    if "client_text" in d:
        for client in d["client_text"]:
            st.caption(f"• {client}")

    st.subheader("Tools Usage")

    df = pd.DataFrame(list(d["tools"].items()), columns=["Tools", "Usage"])
    st.bar_chart(df.set_index("Tools"))

# PAGE NEW CLIENT TRACKER

elif page ==  "New Client Tracker":

    st.title("New Client Tracker")

# =====================================================
# MONTH ORDER
# =====================================================

    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

# =====================================================
# TOTAL NEW CLIENT DATA
# =====================================================

    new_client_df = pd.DataFrame({
        "Month": month_order,
        "Client": [17, 7, 7, 21, 8, 0, 0, 0, 0, 0, 0, 0]
    })

    new_client_df["Month"] = pd.Categorical(
        new_client_df["Month"],
        categories=month_order,
        ordered=True
    )    

    new_client_df = new_client_df.sort_values("Month")
    new_client_df = new_client_df.set_index("Month")

# =====================================================
# SUMATRA CLIENT DATA
# =====================================================

    sumatra_df = pd.DataFrame({
        "Month": month_order,
        "Client": [3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    })

    sumatra_df["Month"] = pd.Categorical(
        sumatra_df["Month"],
        categories=month_order,
        ordered=True
    )

    sumatra_df = sumatra_df.sort_values("Month")
    sumatra_df = sumatra_df.set_index("Month")

# =====================================================
# MAU DATA
# =====================================================

    mau_df = pd.DataFrame({

        "Month": month_order,

        "2025": [
        125, 130, 115, 112,
        133, 135, 138, 147,
        154, 151, 132, 126
        ],

        "2026": [
        148, 137, 118, 178,
        173, 0, 0, 0,
        0, 0, 0, 0
        ]
    })

    mau_df["Month"] = pd.Categorical(
        mau_df["Month"],
        categories=month_order,
        ordered=True
    )

    mau_df = mau_df.sort_values("Month")
    mau_df = mau_df.set_index("Month")

# =====================================================
# CLIENT LIST
# =====================================================

    sumatra_clients = {

        "January": [
        "Biro Optimal",
        "Biro Widya Talenta",
        "Al Chair Consulting"
        ],

        "February": [
        "PP Juliana"
        ],

        "March": [
        "PP Siti Ulfa Hutabarat"
        ],

        "April": [
        "-"
        ],
        
        "May": [
        "-"
        ]
    }

# =====================================================
# TOTAL NEW CLIENT CHART
# =====================================================

    st.subheader("Total New Client 2026")

    st.bar_chart(new_client_df)

# =====================================================
# TOTAL REVENUE
# =====================================================

    new_client_revenue=139764000
    st.metric("Total New Client Revenue", f"Rp{new_client_revenue:,}")


# =====================================================
# MONTHLY ACTIVE USER
# =====================================================

    st.subheader("Monthly Active User 2026")

    st.bar_chart(mau_df)


# =====================================================
# TOTAL NEW CLIENT SUMATRA
# =====================================================

    st.subheader("Total New Client Sumatra 2026")

    st.bar_chart(sumatra_df)


# =====================================================
# CLIENT LIST
# =====================================================

    st.subheader("New Client Sumatra List")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.markdown("### January")

        for client in sumatra_clients["January"]:
            st.markdown(f"• {client}")

    with col2:

        st.markdown("### February")

        for client in sumatra_clients["February"]:
            st.markdown(f"• {client}")

    with col3:

        st.markdown("### March")

        for client in sumatra_clients["March"]:
            st.markdown(f"• {client}")

    with col4:

        st.markdown("### April")

        for client in sumatra_clients["April"]:
            st.markdown(f"• {client}")
            
    with col5:

        st.markdown("### May")

        for client in sumatra_clients["May"]:
            st.markdown(f"• {client}")

        
# PAGE EXPANSION TRACKER
elif page == "Expansion Tracker":

    st.title("Expansion Tracker")

    total_all = sum(sum(prov.values()) for prov in expansion_data.values())
    st.metric("Total Indonesia Client", total_all)

    for island in expansion_data:

        st.subheader(island)

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(image_map[island], width=700)

        with col2:
            table = pd.DataFrame(
                list(expansion_data[island].items()),
                columns=["Province", "Client"]
        )

            total_client = table["Client"].sum()
            percentage = (total_client/total_all)*100

            st.metric(f"{island} Client", total_client, f"{percentage:.0f}% of total")
            st.bar_chart(table.set_index("Province"))

# PAGE 6
elif page == "Faxtor 2026 Calendar":

    import json
    import streamlit.components.v1 as components

    # Semua string pakai ASCII biasa — tidak ada unicode escape atau emoji
    # agar tidak terjadi UnicodeEncodeError di Streamlit Cloud
    events_data = {
        "Jan": [
            {"date": "28", "title": "Annual Business Plan 2026",      "end": "",         "tentative": False, "desc": "All Division"},
        ],
        "Feb": [],
        "Mar": [
            {"date": "1",  "title": "Uji Coba FLSI",            "end": "May",  "tentative": False, "desc": "R&D Fatiya"},
            {"date": "1",  "title": "Penormaan FTPI 2.0",        "end": "May",  "tentative": False, "desc": "R&D Hafi"},
            {"date": "15", "title": "Launching Faxtor Newsletter","end": "",     "tentative": False, "desc": "BA, Marcomm"},
        ],
        "Apr": [
            {"date": "1",  "title": "Uji Coba CDPI-SR",                          "end": "",         "tentative": False, "desc": "R&D Diana"},
            {"date": "1",  "title": "Workshop Item Writer FCAT-2",                "end": "",         "tentative": False, "desc": "R&D Afiya"},
            {"date": "1",  "title": "Test Construction FCAT-2",                   "end": "May",      "tentative": False, "desc": "R&D Afiya"},
            {"date": "1",  "title": "Training Master Excel",                      "end": "June",     "tentative": False, "desc": "R&D Fatiya"},
            {"date": "4",  "title": "Workshop Tester CDPI-SR",                    "end": "",         "tentative": False, "desc": "R&D Diana"},
            {"date": "15", "title": "April Newsletter - Love Bombing di Kantor",  "end": "",         "tentative": False, "desc": "BA, Marcomm, Prof. Aulia"},
            {"date": "18", "title": "Sumatra Webinar Series Vol 01",               "end": "",         "tentative": False, "desc": "BA, Marcomm, PLES"},
            {"date": "21", "title": "Pelatihan dan Evaluasi Psikolog Mitra Batch 1","end": "June",   "tentative": False, "desc": "PLES"},
            {"date": "25", "title": "Program Diskon May Day",                      "end": "May 15",  "tentative": False, "desc": "BA, BS"},
        ],
        "May": [
            {"date": "1",  "title": "Pelatihan dan Evaluasi Biro Mitra Faxtor",   "end": "July",     "tentative": True,  "desc": "PLES"},
            {"date": "4",  "title": "Assessment Center Training",                  "end": "",         "tentative": False, "desc": "All Division"},
            {"date": "15", "title": "Program Biro Juara",                          "end": "",         "tentative": False, "desc": "BA & BS"},
            {"date": "15", "title": "May Newsletter - Syarat Rekrutmen IPK 3.0",   "end": "",         "tentative": False, "desc": "BA, Marcomm, R&D"},
            {"date": "16", "title": "Sumatra Webinar Series Vol 02 - Discoverme",  "end": "",         "tentative": False, "desc": "BA, Marcomm, PLES"},
            {"date": "18", "title": "Faxtor Berkurban 2026",                       "end": "",         "tentative": False, "desc": "HRBP Corporate, HRBP Commercial"},
            {"date": "29", "title": "Ways of Working: New Office, New Habit",      "end": "",         "tentative": False, "desc": "HRBP Corporate, HRBP Commercial"},
            {"date": "30", "title": "Education Webinar with APSI DKI Jakarta",     "end": "",         "tentative": False, "desc": "BA, Marcomm, PLES"},
        ],
        "Jun": [
            {"date": "6", "title": "Project BJB (Geo) Tes Produk",                          "end": "",         "tentative": False,  "desc": "AS"},
            {"date": "13", "title": "Project BJB (Adel) Psikotes & Interview",                          "end": "14 June",         "tentative": False,  "desc": "AS"},
            {"date": "15",  "title": "Perpindahan Kantor Baru",                     "end": "",         "tentative": True,  "desc": "HRBP Corporate"},
            {"date": "15", "title": "Pelatihan dan Evaluasi Psikolog Mitra Batch 2","end": "August",  "tentative": True,  "desc": "PLES"},
            {"date": "15", "title": "Pelatihan dan Evaluasi Psikolog Mitra Batch 3","end": "September","tentative": True, "desc": "PLES"},
            {"date": "15", "title": "June Newsletter - Cybernetic Leadership",      "end": "",         "tentative": False, "desc": "BA, Marcomm, R&D Hafi"},
            {"date": "22", "title": "Mid Year Performance Review - Head / Lead",    "end": "",         "tentative": True,  "desc": "HRBP Corporate"},
        ],
        "Jul": [
            {"date": "13", "title": "Mid Year Performance Review - All Employee",   "end": "August",  "tentative": True,  "desc": "HRBP Corporate"},
            {"date": "13", "title": "Webinar Faxtor FMAT",                          "end": "",         "tentative": True,  "desc": "BA, Marcomm, PLES"},
            {"date": "15", "title": "July Newsletter - Karyawan Penurut vs Pembangkang","end": "",    "tentative": False, "desc": "BA, Marcomm, R&D Nisa"},
            {"date": "18", "title": "Webinar with APIO Jawa Tengah",                "end": "",        "tentative": True,  "desc": "BA, Marcomm, PLES"},
        ],
        "Aug": [
            {"date": "15", "title": "August Newsletter - Asesmen Asal Jadi",       "end": "",        "tentative": False, "desc": "BA, Marcomm, R&D Fatiya"},
        ],
        "Sep": [
            {"date": "15", "title": "September Newsletter - Strategic Problem Solving","end": "",     "tentative": False, "desc": "BA, Marcomm, R&D Afiya"},
        ],
        "Oct": [
            {"date": "15", "title": "October Newsletter - Formula Sukses X+Y+Z",   "end": "",        "tentative": False, "desc": "BA, Marcomm, R&D Diana"},
        ],
        "Nov": [
            {"date": "15", "title": "November Newsletter - The Gender Myth",        "end": "",        "tentative": False, "desc": "BA, Marcomm, R&D Fatiya"},
        ],
        "Dec": [
            {"date": "15", "title": "December Newsletter - Working Memory Capacity","end": "",        "tentative": False, "desc": "BA, Marcomm, R&D Afiya"},
        ],
    }

    # json.dumps dengan ensure_ascii=True agar 100% aman di semua environment
    events_json = json.dumps(events_data, ensure_ascii=True)

    calendar_html = (
        "<!DOCTYPE html><html><head><meta charset='UTF-8'>"
        "<style>"
        "* { box-sizing: border-box; margin: 0; padding: 0; }"
        "body { font-family: 'Source Sans Pro', sans-serif; background: #f7f8fc; padding: 8px 4px; }"
        ".subtitle { font-size: 12px; color: #9ca3af; margin-bottom: 20px; }"
        ".layout { display: flex; gap: 24px; align-items: flex-start; }"
        ".month-panel { width: 200px; flex-shrink: 0; }"
        ".month-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 7px; }"
        ".month-btn {"
        "  background: white; border: 2px solid #dbe2ff; border-radius: 10px;"
        "  padding: 9px 4px; text-align: center; cursor: pointer;"
        "  font-family: inherit; font-size: 11.5px; font-weight: 600; color: #6b7280;"
        "  transition: all 0.15s ease; width: 100%; line-height: 1.3;"
        "}"
        ".month-btn:hover { border-color: #ff4b5c; color: #ff4b5c; background: #fff5f6; }"
        ".month-btn.active { background: #ff4b5c; border-color: #ff4b5c; color: white; box-shadow: 0 4px 12px rgba(255,75,92,.3); }"
        ".month-btn.empty { opacity: .4; cursor: default; }"
        ".month-btn.empty:hover { border-color: #dbe2ff; color: #6b7280; background: white; }"
        ".month-btn .count { display: block; font-size: 9.5px; font-weight: 400; margin-top: 2px; opacity: .75; }"
        ".events-panel { flex: 1; min-width: 0; }"
        ".panel-header { font-size: 26px; font-weight: 700; color: #1f2937; margin-bottom: 2px; }"
        ".panel-count { font-size: 12px; color: #9ca3af; margin-bottom: 16px; }"
        ".no-events { color: #d1d5db; font-size: 13px; font-style: italic; }"
        ".event-row { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 10px; }"
        ".date-chip {"
        "  min-width: 48px; height: 48px; background: #ff4b5c; border-radius: 10px;"
        "  display: flex; align-items: center; justify-content: center;"
        "  font-size: 19px; font-weight: 700; color: white; flex-shrink: 0;"
        "  box-shadow: 0 3px 8px rgba(255,75,92,.25);"
        "}"
        ".event-card {"
        "  background: white; border-radius: 10px; padding: 10px 14px;"
        "  flex: 1; border: 1px solid #e5e7eb; min-width: 0;"
        "  box-shadow: 0px 2px 6px rgba(0,0,0,0.04);"
        "}"
        ".event-title { font-size: 13px; font-weight: 700; color: #1f2937; line-height: 1.4; }"
        ".event-badges { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px; }"
        ".badge { display: inline-block; font-size: 10px; font-weight: 600; border-radius: 5px; padding: 2px 7px; }"
        ".badge-end { background: #fff0f2; color: #ff4b5c; }"
        ".badge-tentative { background: #fff8e1; color: #d97706; }"
        ".event-desc { font-size: 11px; color: #9ca3af; margin-top: 4px; }"
        ".divider { height: 1px; background: #f3f4f6; margin: 3px 0 10px 0; }"
        "</style></head><body>"
        "<p class='subtitle'>Click month to view detailed events. "
        "<div class='layout'>"
        "<div class='month-panel'><div class='month-grid' id='grid'></div></div>"
        "<div class='events-panel' id='panel'></div>"
        "</div>"
        "<script>"
        "var events = " + events_json + ";"
        "var months = Object.keys(events);"
        "var selected = 'May';"
        "function renderGrid() {"
        "  var grid = document.getElementById('grid');"
        "  grid.innerHTML = '';"
        "  months.forEach(function(m) {"
        "    var n = events[m].length;"
        "    var btn = document.createElement('button');"
        "    btn.className = 'month-btn' + (n === 0 ? ' empty' : '') + (m === selected ? ' active' : '');"
        "    btn.innerHTML = m + '<span class=\"count\">' + n + ' event' + (n !== 1 ? 's' : '') + '</span>';"
        "    if (n > 0) { btn.onclick = (function(mo) { return function() { selected = mo; renderGrid(); renderPanel(); }; })(m); }"
        "    grid.appendChild(btn);"
        "  });"
        "}"
        "function renderPanel() {"
        "  var panel = document.getElementById('panel');"
        "  var list = events[selected];"
        "  var html = '<div class=\"panel-header\">' + selected + '</div>';"
        "  html += '<div class=\"panel-count\">' + list.length + ' scheduled event' + (list.length !== 1 ? 's' : '') + '</div>';"
        "  if (list.length === 0) {"
        "    html += '<div class=\"no-events\">Tidak ada event di bulan ini.</div>';"
        "  } else {"
        "    list.forEach(function(ev, i) {"
        "      var badges = '';"
        "      if (ev.tentative) badges += '<span class=\"badge badge-tentative\">Tentative</span>';"
        "      if (ev.end) badges += '<span class=\"badge badge-end\">ends ' + ev.end + '</span>';"
        "      var badgesHtml = badges ? '<div class=\"event-badges\">' + badges + '</div>' : '';"
        "      var divider = i < list.length - 1 ? '<div class=\"divider\"></div>' : '';"
        "      html += '<div class=\"event-row\">' +"
        "        '<div class=\"date-chip\">' + ev.date + '</div>' +"
        "        '<div class=\"event-card\">' +"
        "          '<div class=\"event-title\">' + ev.title + '</div>' +"
        "          badgesHtml +"
        "          '<div class=\"event-desc\">' + ev.desc + '</div>' +"
        "        '</div>' +"
        "      '</div>' + divider;"
        "    });"
        "  }"
        "  panel.innerHTML = html;"
        "}"
        "renderGrid();"
        "renderPanel();"
        "</script></body></html>"
    )

    # Hilangkan border biru dari iframe components.html
    st.markdown("""
        <style>
        iframe { border: none !important; outline: none !important; }
        </style>
    """, unsafe_allow_html=True)

    st.title("Faxtor 2026 Calendar")
    components.html(calendar_html, height=900, scrolling=True)


# PAGE 3

elif page == "Royalty Calculator":

    st.title("Royalty Calculator")

    mode = st.radio("Royalty Scheme", ["Percentage-based", "Fixed Number"])

    table = pd.DataFrame(
        list(royalty_pricing.items()),
        columns=["Product", "Price"]
    )

    if mode == "Percentage-based":
        rate = st.slider("Royalty Rate (%)", 0, 100, 30)
        rate = rate / 100

        table["Royalty"] = (table["Price"] * rate).astype(int)

    else:
        fixed = st.slider("Fixed Number (Rp)", 0, 50000, 10000)
        table["Royalty"] = fixed

    table["Server Cost"] = 10000

    table["Margin (%)"] = (
        (table["Price"] - table["Royalty"] - table["Server Cost"])
        / table["Price"] * 100
    ).round(0).astype(int)

  
    # STYLING TABLE
   
    styled_table = table.style.set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#dbe2ff"),  # biru muda
                ("color", "#2c3e50"),
                ("font-weight", "bold")
            ]
        }
    ])

    styled_table = styled_table.format({
        "Price": "Rp{:,.0f}",
        "Royalty": "Rp{:,.0f}",
        "Server Cost": "Rp{:,.0f}"
    })

    
    # OUTPUT
    
    st.subheader("Royalty Table")
    st.dataframe(styled_table)


# PAGE 5

elif page == "Sales Forecaster":

    st.title("Sales Forecaster")

    mode = st.radio(
        "Choose Pricing Setup",
        ["Standard Enterprise", "Professional Enterprise"]
    )

    pricing = standard_pricing if mode == "Standard Enterprise" else professional_pricing

    st.metric("Monthly Gross Target", f"Rp{gross_target:,}")

    col1, col2 = st.columns([1,1])

    quantity = {}
    data = []
    total_revenue = 0

    with col1:
        st.subheader("Sales Volume")

        for product in pricing:

            col_img, col_slider = st.columns([1,3])

            with col_img:
                if product in logo_map:
                    st.image(logo_map[product], width=70)
                    st.caption(product)  # optional biar tetap kebaca
                else:
                    st.markdown(f"**{product}**")

            with col_slider:
                quantity[product] = st.slider(
                    label="",
                    min_value=0,
                    max_value=50000,
                    value=0,
                    step=5,
                    key=product
                )

    for product in pricing:
        price = pricing[product]
        qty = quantity[product]
        revenue = price * qty

        total_revenue += revenue

        data.append({
            "Product": product,
            "Price": price,
            "Quantity": qty,
            "Revenue": revenue
        })

    df = pd.DataFrame(data)
    achievement = (total_revenue / gross_target) * 100

    with col2:
        st.subheader("Total Revenue")

        st.metric(
            label="",
            value=f"Rp{total_revenue:,}",
            delta=f"{achievement:.0f}% of target"
        )

        st.bar_chart(df.set_index("Product")["Revenue"])


