from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Dipesh Silwal",
    description="A small package for Which Bollywood Celebrity You look like? Deep Learning Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dipesg/Which_Bollywood_Celebrity_You_Look_Like",
    author_email="entbappy73@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'mtcnn',
        'tensorflow-cpu==2.1.0',
        'keras==2.2.4',
        'keras-vggface==0.6',
        'keras_applications==1.0.8',
        'opencv-python-headless==4.2.0.32',
        'PyYAML',
        'tqdm',
        'scikit-learn',
        'streamlit',
        'bing-image-downloader'
    ]
)
