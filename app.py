import streamlit as st

# Initialize session state for buttons
if 'active_button' not in st.session_state:
    st.session_state.active_button = None

# Create the "External Site" and "Show Filters" buttons
if st.sidebar.button("External Site"):
    st.session_state.active_button = "external_site"

if st.sidebar.button("Show Filters"):
    st.session_state.active_button = "show_filters"

# Custom CSS and JavaScript to adjust iframe based on sidebar state
css_js = """
    <style>
        .full-iframe-container {
            position: fixed;
            top: 3.5rem;  /* Adjust top to be below Streamlit header */
            left: 17rem;  /* Initial left position when sidebar is expanded */
            width: calc(100% - 17rem); /* Initial width when sidebar is expanded */
            height: calc(100% - 3.5rem); /* Adjust height to not overlap the header */
            margin: 0;
            padding: 0;
            overflow: hidden;
            z-index: 1;
            transition: left 0.3s, width 0.3s; /* Smooth transition for sidebar toggle */
        }
        .full-iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        /* Adjust the padding of Streamlit app content */
        .main .block-container {
            padding: 0;
        }
    </style>
    <script>
        // Function to adjust iframe position based on sidebar state
        function adjustIframe() {
            const iframeContainer = document.querySelector('.full-iframe-container');
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            if (sidebar && iframeContainer) {
                const sidebarStyle = window.getComputedStyle(sidebar);
                if (sidebarStyle.transform === 'none') {
                    // Sidebar is expanded
                    iframeContainer.style.left = '17rem';
                    iframeContainer.style.width = 'calc(100% - 17rem)';
                } else {
                    // Sidebar is collapsed
                    iframeContainer.style.left = '0';
                    iframeContainer.style.width = '100%';
                }
            }
        }

        // Initial adjustment
        window.addEventListener('DOMContentLoaded', adjustIframe);

        // Adjust iframe whenever the window is resized (in case sidebar is toggled)
        window.addEventListener('resize', adjustIframe);

        // Observe sidebar changes
        const observer = new MutationObserver(adjustIframe);
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            observer.observe(sidebar, { attributes: true, attributeFilter: ['style'] });
        }
    </script>
"""

# Inject the custom CSS and JavaScript into the app
st.markdown(css_js, unsafe_allow_html=True)

# Main content area
if st.session_state.active_button == "external_site":
    st.markdown("<div class='full-iframe-container'><iframe src='https://app.powerbi.com/reportEmbed?reportId=4b89fc6e-6b76-4aee-b58c-b3048eb29fc3&autoAuth=true&ctid=29656626-bbab-4437-ba66-213753425fd1' class='full-iframe'></iframe></div>", unsafe_allow_html=True)
elif st.session_state.active_button == "show_filters":
    st.title("Filters")
    with st.expander("Filters"):
        option1 = st.selectbox("Option 1", ["A", "B", "C"])
        option2 = st.multiselect("Option 2", ["X", "Y", "Z"])
        date_range = st.date_input("Select Date Range", [])
        st.write("Selected filters:")
        st.write(f"Option 1: {option1}")
        st.write(f"Option 2: {option2}")
        st.write(f"Date Range: {date_range}")
else:
    st.write("Select an option from the sidebar.")
