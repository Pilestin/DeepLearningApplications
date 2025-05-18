css_string = """
<style>
    .news-card {
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
        background-color: white;
    }
    .news-card:hover {
        transform: translateY(-5px);
    }
    .news-image {
        width: 100%;
        border-radius: 0.3rem;
        margin-bottom: 0.5rem;
    }
    .news-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .news-source {
        font-size: 0.8rem;
        color: #888;
        margin-bottom: 0.5rem;
    }
    .news-date {
        font-size: 0.8rem;
        color: #888;
        margin-bottom: 0.5rem;
    }
    .news-summary {
        font-size: 0.9rem;
        color: #333;
        margin-bottom: 0.5rem;
    }
    .news-actions {
        display: flex;
        justify-content: space-between;
        margin-top: 0.5rem;
    }
    .summary-header {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .summary-item {
        padding: 0.8rem;
        border-left: 3px solid #4CAF50;
        background-color: #f9f9f9;
        margin-bottom: 0.8rem;
    }
    .stButton button {
        width: 100%;
    }
    .category-selector {
        margin-bottom: 1rem;
    }
    .app-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .loading-spinner {
        text-align: center;
        margin: 2rem;
    }
</style>
"""