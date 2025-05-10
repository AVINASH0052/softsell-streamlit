# SoftSell - Software License Marketplace

A responsive, single-page marketing website for a fictional software resale startup built with Streamlit.

## Features

- Modern, responsive design
- Interactive chat widget powered by NVIDIA's LLM
- Contact form with frontend validation
- Customer testimonials
- How it works section
- Why choose us section

## Tech Stack

- Streamlit for the web application
- NVIDIA's LLM API for the chat functionality
- Python for backend logic
- Custom CSS for styling

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Get your NVIDIA API key:**
   - Go to [NVIDIA API Portal](https://platform.nvidia.com/)
   - Sign up or log in
   - Create an API key for the LLM service
   - Copy your API key (it will look like `nvapi-...`)
5. **Create a `.env` file in the project root:**
   ```
   NVIDIA_API_KEY=your-nvidia-key-here
   ```
6. Run the application:
   ```bash
   streamlit run app.py
   ```

## Security Note
- **Never commit your `.env` file or API key to GitHub.**
- The `.env` file is included in `.gitignore` by default.

## Design Choices

- Used Streamlit for rapid development and easy deployment
- Implemented a clean, modern UI with consistent spacing and typography
- Added interactive elements like the chat widget for better user engagement
- Used a responsive layout that works well on all device sizes
- Implemented a dark theme for better readability and modern feel

## Time Spent

- Initial setup and structure: 1 hour
- UI implementation: 2 hours
- Chat functionality: 1 hour
- Testing and refinement: 1 hour
- Total: 5 hours

## Future Improvements

- Add dark/light mode toggle
- Implement more animations
- Add more interactive elements
- Enhance SEO meta tags
- Add analytics tracking 