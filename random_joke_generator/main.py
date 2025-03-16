import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        # Make GET request to the API
        response=requests.get("https://official-joke-api.appspot.com/random_joke")
        
        # Check if the request is successful
        if response.status_code==200:
            # Parse the JSON response
            joke_data=response.json()
            # Return formatted joke with setup and punchline (dictionary keys)
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            # Return error message if API call fails
            return "Failed to fetch joke from API"
    except:
        # Return fallback joke if exception occurs like interner
        return "Why don't scientists trust atoms? Because they make up everything!"

def main():
    print("Hello from random-joke-generator!")
    # set page title
    st.title("Random Joke Generator")
    # Add instruction text
    st.write("Click the button below to generate a random joke")
    # Create a button and handle click
    if st.button("Generate Random Joke"):
        joke=get_random_joke()
        st.success(joke)
    st.divider()

    st.markdown(
        """
        <div style='text-align:center'>
        <p>Joke from Official Joke API</p>
        <p>Build with ❤️ by <a href='https://github.com/umair-jami'>Umair Jami</a> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
