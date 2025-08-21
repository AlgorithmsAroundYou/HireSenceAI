# Author: Sai Kumar Kodati
#

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Agiliad AI Apps",
        page_icon="🏚",
        layout="wide"
    )

    st.balloons()
    st.info('This is a purely demo applications', icon="ℹ️")
    st.write("# Welcome to Agiliad AI Apps! 👋")
    st.snow()

    st.markdown(
        """
        Agiliad AI Apps is a collection of applications that leverage the power of AI to solve various problems.

        ## Features
        - **AI-Powered Solutions**: Explore applications that utilize AI to enhance productivity and creativity.
        - **User-Friendly Interface**: Designed for ease of use, making it accessible for everyone.
        - **Open Source**: All applications are open source, encouraging collaboration and innovation.    
        """
    )


if __name__ == "__main__":
    run()