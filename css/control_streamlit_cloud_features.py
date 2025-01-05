
hide_streamlit_style = """
        <style>
        # div[data-testid="stToolbar"] {
        # visibility: hidden;
        # height: 0%;
        # position: fixed;
        # }
        # div[data-testid="stDecoration"] {
        # visibility: hidden;
        # height: 0%;
        # position: fixed;
        # }
        # div[data-testid="stStatusWidget"] {  //hide streamlit runner
        # visibility: hidden;
        # height: 0%;
        # position: fixed;
        }
        # #MainMenu {
        # visibility: hidden;
        # height: 0%;
        # # }
        # header {
        # visibility: hidden;
        # height: 0%;
        # }
        # footer {
        # visibility: hidden;
        # height: 0%;
        # }
        </style>
        """