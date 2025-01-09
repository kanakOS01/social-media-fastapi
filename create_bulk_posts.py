import requests

# List of posts to publish
trial_posts = [
    {
        "title": "Learning JavaScript",
        "content": "The basics of JavaScript and how to get started.",
    },
    {
        "title": "Gardening Tips for Beginners",
        "content": "How to start your own garden and keep plants healthy.",
    },
    {
        "title": "Exploring Quantum Computing",
        "content": "An introduction to quantum computers and their applications.",
    },
    {
        "title": "The Joy of Reading",
        "content": "Why reading books can improve your mental health and creativity.",
    },
    {
        "title": "Cooking Quick Meals",
        "content": "Simple recipes for delicious meals in under 30 minutes.",
    },
    {
        "title": "The Future of Renewable Energy",
        "content": "Exploring the advancements in renewable energy sources.",
    },
    {
        "title": "Time Management Tips",
        "content": "How to manage your time effectively to boost productivity.",
    },
    {
        "title": "Understanding 5G Technology",
        "content": "What is 5G, and how does it impact our daily lives?",
    },
    {
        "title": "The Basics of Cryptocurrency",
        "content": "A beginner's guide to understanding Bitcoin and other cryptocurrencies.",
    },
    {
        "title": "Stress Management Techniques",
        "content": "Practical tips to reduce stress and improve your well-being.",
    },
    {
        "title": "Creating a Minimalist Lifestyle",
        "content": "How to simplify your life and focus on what matters.",
    },
    {
        "title": "The Power of Networking",
        "content": "Why building relationships is crucial for career growth.",
    },
    {
        "title": "AI in Healthcare",
        "content": "How artificial intelligence is revolutionizing the medical field.",
    },
    {
        "title": "The History of the Internet",
        "content": "Tracing the development of the internet from its inception.",
    },
    {
        "title": "Mindful Morning Routines",
        "content": "Start your day right with a mindful and productive routine.",
    },
    {
        "title": "The Rise of AI",
        "content": "Exploring how artificial intelligence is shaping the future.",
    },
    {
        "title": "10 Best Python Libraries",
        "content": "A curated list of Python libraries for data science and machine learning.",
        "published": False,
    },
    {
        "title": "Understanding Blockchain",
        "content": "A beginner's guide to how blockchain technology works.",
    },
    {
        "title": "Healthy Eating Tips",
        "content": "Simple tips to maintain a balanced and nutritious diet.",
        "published": False,
    },
    {
        "title": "Exploring Space",
        "content": "The latest discoveries and missions in the realm of space exploration.",
    },
    {
        "title": "How to Start Coding",
        "content": "Steps and resources for beginners to learn programming.",
    },
    {
        "title": "The Art of Meditation",
        "content": "Techniques and benefits of practicing mindfulness.",
        "published": False,
    },
    {
        "title": "Web Development Trends",
        "content": "The top trends to watch in web development this year.",
    },
    {
        "title": "Travel on a Budget",
        "content": "Tips for exploring the world without breaking the bank.",
        "published": False,
    },
    {
        "title": "Fitness at Home",
        "content": "Effective exercises you can do without going to the gym.",
    },
    {
        "title": "The History of Programming",
        "content": "An overview of how programming languages have evolved.",
    },
    {
        "title": "Investing for Beginners",
        "content": "A simple guide to understanding the basics of investing.",
        "published": False,
    },
    {
        "title": "Photography Tips",
        "content": "How to capture stunning photos using a smartphone.",
    },
    {
        "title": "Understanding Climate Change",
        "content": "What you need to know about the impacts of climate change.",
    },
    {
        "title": "Mastering Public Speaking",
        "content": "Tips to boost confidence and improve your public speaking skills.",
        "published": False,
    },
]

api_url = "http://localhost:8000/posts/"
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo3LCJleHAiOjE3MzQ2OTExMjB9.7F9hZAUbL7bGgvMkx6pLkGXd5bIP2mS_QZgmkukglXA"
headers = {"Authorization": f"Bearer {jwt_token}"}


def publish_posts(posts, api_url):
    for post in trial_posts:
        response = requests.post(api_url, json=post, headers=headers)
        if response.status_code == 201:
            print(f"Post '{post['title']}' created successfully.")
        else:
            print(f"Failed to create post '{post['title']}': {response.status_code}, {response.text}")


publish_posts(trial_posts, api_url)
