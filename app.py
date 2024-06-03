import streamlit as st
import streamlit.components.v1 as components

#import altair as alt
#import plotly.express as px





#######################
# Page configuration
st.set_page_config(
    page_title="Inquiry Insights App",
    page_icon="Input_data/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

logo_path = "Input_data/Inquiry_Insights_Dashboard_Logo_Sidebar.png"

# CSS
css = """
<style>
    section[data-testid="stSidebar"] {
        width: 290px !important; 
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    section[data-testid="stImage"] {
        width: 50px !important;
        height: 50px !important;
    }
    .full-iframe-container {
        position: fixed;
        top: 3.5rem;
        left: 299px;
        width: calc(100% - 299px);
        height: calc(100% - 3.5rem);
        margin: 0;
        padding: 0;
        overflow: hidden;
        z-index: 1;
        transition: left 0.3s, width 0.3s;
    }
    .full-iframe-container.collapsed {
        left: 50px;
        width: calc(100% - 50px);
    }
    .full-iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
    .stButton button {
        background-color: #f0f0f0;
        border: none;
        color: black;
        padding: 10px 20px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        width: 250px;
    }
    [data-testid="stSidebar"] img {
        margin-top: -60px !important;
    }
    [data-testid="element-container"]:empty {
        display: none;
    }
</style>
"""

js_code = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const targetNode = parent.document.querySelector('[data-testid="stSidebar"]');
        const observer = new MutationObserver((mutations) => {
            const iframeContainer = parent.document.querySelector('.full-iframe-container');
            mutations.forEach((mutation) => {
                if (mutation.attributeName === 'aria-expanded') {
                    if (targetNode.getAttribute('aria-expanded') === 'false') {
                        iframeContainer.classList.add('collapsed');
                    } else {
                        iframeContainer.classList.remove('collapsed');
                    }
                }
            });
        });
        observer.observe(targetNode, {
            attributes: true,
            attributeFilter: ['aria-expanded'],
        });
    });
</script>
"""

#######################
# Load data and preprocessing



#######################
# Sidebar and filters

st.markdown(css, unsafe_allow_html=True)


# Initialize session state for buttons and filters visibility
if 'active_button' not in st.session_state:
    st.session_state.active_button = "intractive_dashboard"
if 'show_filters' not in st.session_state:
    st.session_state.show_filters = False

# Function to set the active button and its state
def set_active_button(button_name):
    st.session_state.active_button = button_name
    st.session_state.show_filters = button_name == "custom_live_dashboard"

with st.sidebar:
    st.sidebar.image("Input_data/Inquiry_Insights_Dashboard_Logo_Sidebar_white_nobg.png", use_column_width=True)
    
    if st.sidebar.button("Intractive Dashboard", key="btn_intractive_dashboard"):
        set_active_button("intractive_dashboard")
    if st.sidebar.button("Custom Live Dashboard", key="btn_live_dashboard"):
        set_active_button("custom_live_dashboard")

    if st.session_state.get('show_filters', False):
        start_date = st.date_input('Start date', format="DD/MM/YYYY")
        end_date = st.date_input('End date', format="DD/MM/YYYY")

        



def ChangeButtonColour(widget_label, prsd_status):
    btn_bg_colour = "#64B5F6" if prsd_status else "#f0f0f0"
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{
                if (elements[i].innerText == '{widget_label}') {{
                    elements[i].style.background = '{btn_bg_colour}';
                }}
            }}
        </script>
    """
    components.html(htmlstr, height=0, width=0)

def ChkBtnStatusAndAssignColour():
    btn_labels = ["Intractive Dashboard", "Custom Live Dashboard"]
    for label in btn_labels:
        ChangeButtonColour(label, st.session_state.get('active_button') == label.lower().replace(" ", "_"))





ChkBtnStatusAndAssignColour()

if st.session_state.get('show_filters', False):
    st.title("Select an option from the sidebar.")
elif st.session_state.get('active_button') == "intractive_dashboard":
    st.markdown("<div class='full-iframe-container'><iframe src='https://app.powerbi.com/reportEmbed?reportId=4b89fc6e-6b76-4aee-b58c-b3048eb29fc3&autoAuth=true&ctid=29656626-bbab-4437-ba66-213753425fd1&navContentPaneEnabled=false' class='full-iframe'></iframe></div>", unsafe_allow_html=True)


components.html(js_code, height=0)
