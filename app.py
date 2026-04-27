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
            "Expansion Tracker",
            "Royalty Calculator",
            "Sales Forecaster",
            "Faxtor 2026 Calendar"
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

revenue_actual=2437661932
revenue_target=9000000000
profit_actual=755626322
profit_target=3600000000

expansion_data = {
    "Jawa":{"Banten":50,"DIY":16,"DKI Jakarta":158,"Jawa Barat":223,"Jawa Tengah":19,"Jawa Timur":32},
    "Sumatra":{"Aceh":7,"Bangka Belitung":2,"Jambi":2,"Kep. Riau":5,"Lampung":4,"Riau":4,"Sumatra Barat":7,"Sumatra Selatan":3,"Sumatra Utara":23},
    "Kalimantan":{"Kalimantan Barat":3,"Kalimantan Selatan":1,"Kalimantan Tengah":4,"Kalimantan Timur":8,"Kalimantan Utara":2},
    "Sulawesi":{"Sulawesi Tenggara":4,"Sulawesi Selatan":5},
    "BaliNusra":{"Bali":8,"NTB":2},
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

    # =========================
    # DATA
    # =========================
    data = {
        "January": {
            "gross": 104,
            "gross_nominal": "Rp780.106.932",
            "gross_insight": "We successfully surpassed the Gross Target by 104% (Rp780.106.932).",

            "nett": 85,
            "nett_nominal": "Rp254.435.608",
            "nett_insight": "Though we achieved Gross Target, minimum Nett Income is Rp300.000.000 / month, yet we have -15% shortfall due to high operational cost.",

            "growth_lm": 24,
            "growth_lm_text": "vs Gross LM Dec’25 (Rp631.020.560)",

            "growth_ytd": 250,
            "growth_ytd_text": "vs Gross YTD Jan’25 (Rp295.485.500)",

            "client": 17,

            "tools": {
                "FCAT": 581, "FCATs": 1171, "FCAT-R": 27, "FTPI": 1107,
                "BIG FIVE": 524, "FEAST": 3403, "LSSI": 262, "IAMAR": 48,
                "PII": 98, "EII": 138, "INCRITS": 45, "OPTI": 117,
                "MSSQ": 27, "MSDQ": 28, "GWS": 3
            }
        },

        "February": {
            "gross": 133,
            "gross_nominal": "Rp1.001.103.500",
            "gross_insight": "We successfully surpass the Gross Target by 133% (Rp1,003,401,500).",

            "nett": 66,
            "nett_nominal": "Rp198.997.492",
            "nett_insight": "Though we achieved Gross Target, minimum Nett Income is Rp300.000.000 / month, yet we have -34% shortfall due to high operational cost (Kimia Farma Project).",

            "growth_lm": 29,
            "growth_lm_text": "vs Gross LM Jan’26 (Rp780.106.932)",

            "growth_ytd": 238,
            "growth_ytd_text": "vs Gross YTD Feb’25 (Rp421.875.500)",

            "client": 7,

            "tools": {
                "FCAT": 3305, "FCATs": 1755, "FCAT-R": 45, "FTPI": 1778,
                "BIG FIVE": 989, "FEAST": 5285, "LSSI": 134, "IAMAR": 36,
                "PII": 918, "EII": 64, "INCRITS": 2364, "OPTI": 2888,
                "MSSQ": 239, "MSDQ": 232, "GWS": 7
            }
        },

        "March": {
            "gross": 88,
            "gross_nominal": "Rp657.941.500",
            "gross_insight": "We partially surpass the Gross Target by 88% (Rp657.941.500).",

            "nett": 74,
            "nett_nominal": "Rp222.281.620",
            "nett_insight": "With minimum Nett Income is Rp300.000.000 / month, yet we have -26% shortfall due to high operational cost.",

            "growth_lm": -34,
            "growth_lm_text": "vs Gross LM Feb’26 (Rp1.001.103.500)",

            "growth_ytd": 87,
            "growth_ytd_text": "vs Gross YTD Mar’25 (Rp351.598.000)",

            "client": 7,

            "tools": {
                "FCAT": 540, "FCATs": 610, "FCAT-R": 538, "FTPI": 1095,
                "BIG FIVE": 939, "FEAST": 19357, "LSSI": 34, "IAMAR": 18,
                "PII": 28, "EII": 35, "INCRITS": 261, "OPTI": 347,
                "MSSQ": 37, "MSDQ": 24, "GWS": 1
            }
        }
    }

    # =========================
    # MONTH SELECTOR
    # =========================
    month = st.radio("Choose Month", list(data.keys()))
    d = data[month]

    # =========================
    # DONUT FUNCTION (FIXED)
    # =========================
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

    # =========================
    # LAYOUT
    # =========================
    col1, col2, col3 = st.columns([2,2,1])

    # =========================
    # GROSS
    # =========================
    with col1:
        st.subheader("GROSS TARGET")
        st.pyplot(donut(d["gross"]))
        st.markdown(f"**{d['gross_nominal']}**")
        st.caption(d["gross_insight"])

    # =========================
    # NETT
    # =========================
    with col2:
        st.subheader("NETT TARGET")
        st.pyplot(donut(d["nett"]))
        st.markdown(f"**{d['nett_nominal']}**")
        st.caption(d["nett_insight"])

    # =========================
    # GROWTH (WITH IMAGE)
    # =========================
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

    # =========================
    # NEW CLIENT
    # =========================
    st.subheader("New Client")
    st.markdown(f"## {d['client']}")

    # =========================
    # TOOLS USAGE
    # =========================
    st.subheader("Tools Usage")

    df = pd.DataFrame(list(d["tools"].items()), columns=["Tools", "Usage"])
    st.bar_chart(df.set_index("Tools"))

# PAGE 3
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


# PAGE 4

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

# PAGE 6
elif page == "Faxtor 2026 Calendar":

    st.title("Faxtor 2026 Calendar")

    events = {
        "April": [
            {"date": "15", "title": "April Newsletter “Love Bombing di Kantor”", "desc": "BA, Marcomm, R&D"},
            {"date": "18", "title": "Sumatra Webinar Series Vol 01 with APIO Sumatra Barat & APIO Lampung", "desc": "BA, Marcomm, R&D"},
            {"date": "25", "title": "[START] Program Diskon May Day", "desc": "BA, BS"},
        ],
        "May": [
            {"date": "4", "title": "[START] Assessment Center Training", "desc": "All Division"},
            {"date": "15", "title": "[START] Program Biro Juara", "desc": "BA & BS"},
            {"date": "15", "title": "May Newsletter “Syarat Rekrutmen IPK 3.0”", "desc": "BA, Marcomm, R&D"},
            {"date": "16", "title": "Sumatra Webinar Series Vol 02 with Discoverme", "desc": "BA, Marcomm, PLES"},
            {"date": "30", "title": "Education Webinar with Asosiasi Psikolog Pendidikan Indonesia (APSI) DKI Jakarta", "desc": "BA, Marcomm, PLES"},
        ],
        "June": [
            {"date": "15", "title": "June Newsletter “Cybernetic Leadership”", "desc": "BA, Marcomm, R&D"},
        ],
        "July": [
            {"date": "15", "title": "July Newsletter “Karyawan Penurut vs Pembangkang”", "desc": "BA, Marcomm, R&D"},
            {"date": "18", "title": "[TENTATIVE] Webinar with APIO Jawa Tengah", "desc": "BA, Marcomm, R&D"},
        ],
    }

    # CUSTOM CSS
    st.markdown("""
        <style>
        .date-box {
            background-color: #f55164;
            color: white;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            border-radius: 8px;
        }

        .event-card {
            background-color: #e5e7eb;
            padding: 15px;
            border-radius: 8px;
        }

        .event-title {
            font-size: 18px;
            font-weight: 600;
            color: #2c3e50;
        }

        .event-desc {
            font-size: 14px;
            color: #6b7280;
        }
        </style>
    """, unsafe_allow_html=True)

    for month, month_events in events.items():

        st.subheader(month)

        for event in month_events:
            col1, col2 = st.columns([1, 5])

            with col1:
                st.markdown(f"""
                    <div class="date-box">
                        {event['date']}
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class="event-card">
                        <div class="event-title">{event['title']}</div>
                        <div class="event-desc">{event['desc']}</div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
