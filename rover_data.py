import streamlit as st
import random

# Function to generate random temperature
def generate_temperature():
    return round(random.uniform(29, 35), 2)

# Function to generate random pressure
def generate_pressure():
    return random.randint(1000, 1018)

# Main function
def main():
    # Set page title and favicon
    st.set_page_config(page_title="Rover Data", page_icon=":partly_sunny:")

    # Set page title
    st.title('Rover Data')

    # Generate weather data
    temperature = generate_temperature()
    pressure = generate_pressure()

    # Display temperature card
    st.markdown(
        f"""
        <div style='background-color: #333333; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1); margin-bottom: 20px;'>
            <h2 style='text-align: center; color: #ffffff;'>Temperature</h2>
            <p style='font-size: 24px; text-align: center; color: #ffffff;'>{temperature} °C</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display pressure card
    st.markdown(
        f"""
        <div style='background-color: #333333; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1); margin-bottom: 20px;'>
            <h2 style='text-align: center; color: #ffffff;'>Pressure</h2>
            <p style='font-size: 24px; text-align: center; color: #ffffff;'>{pressure} hPa</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Auto refresh using JavaScript
    st.markdown(
        """
        <script>
        setInterval(function(){
            window.location.href = window.location.href.split("?")[0] + "?refresh=1";
        }, 30000);
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
