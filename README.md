# Vanlife Blogging Platform

This project is a website or application designed for vanlife enthusiasts. It creates a space for individuals passionate about vanlife to share their van-building knowledge, travel stories, tips, and experiences with a like-minded community. Users can initiate joureys inviting others, and/or create content related to the vanlife culture.

## Prerequisites
Please ensure your Python version is upgraded. For compatibility, although I used Django 5.0.6, my requirements will install 4.2.13 which supports older Python versions. The following steps will guide you through setting up the project with a virtual environment.

## Installation

1. After cloning the repo, please create a virtual environment in the directory containing `requirements.txt`:
    - On Windows:
    ```bash
    python -m venv venv
    ```
    - On macOS and Linux:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Navigate to vanlife_blog directory (where manage.py is) to apply the migrations and start the server:
    ```bash
    python manage.py runserver
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:8000/` to view the project.

### Running Tests

6. To run the tests, use the following command:
    ```bash
    pytest --ds=vanlife_blog.settings --cache-clear


## Target Audience

The platform caters to a broad audience within the vanlife community:

* **Experienced Vanlifers:** Share their journeys, document adventures, and offer insights for others.
* **New Vanlifers:** Seek information, advice, and inspiration for embarking on their vanlife journeys. 
* **Van Builders:** Showcase their van builds and conversion experiences. 
* **Aspiring Vanlifers:** Gain inspiration, tips, and knowledge about building vans and understanding the vanlife lifestyle.
* **Vanlife Curious:** Anyone interested in learning about vanlife culture, popular destinations, and unique travel experiences.

## Main Features

* **User Registration and Login:** Create an account to actively participate in the platform by sharing content and engaging with the community.
* **Route Blog Creation:** Document vanlife adventures, detailing destinations and valuable tips through blog posts.
* **Content Discovery:** Explore a dynamic feed showcasing blog posts from various users.
* **Spot Reference:** Share must-see and must-avoid locations with fellow vanlifers, including specific references and comments.
* **Community Interaction:** Post planned journeys and invite other vanlifers with similar interests to join your adventures.

## Networking Features

* **Client-Server Communication:** The platform leverages a client-server architecture. Users (clients) interact with the server to perform actions like creating accounts, posting content, and viewing other users' content.

## Database Usage

* **User Data:** Stores user account information for authentication and personalization.
* **Blog Content:** Stores details and content of blog posts created by users.
* **Social Interactions:** Stores information about planned trips and user invitations for fostering connections within the community.

## External Libraries

The platform's development will involve utilizing various external libraries:

* **Frontend Design:** Bootstrap for creating a user-friendly and responsive user interface.
* **Backend Development:** Flask or Django (depending on feasibility and learning opportunities) for handling server-side logic and communication.
* **API and Social Integration:** Implementation inspired by previous assignments and potential integration of social media APIs for broader reach.

## Overview

An accompanying image (not included in this markdown document) would visually represent the system's architecture:

* **Clients (Web Browsers):** The user interface where users interact with the platform's features.
* **Server:** The core of the application, handling logic, user requests, and communication with the database. 
* **Database:** The central storage unit for all application data.

This vanlife blogging platform aims to foster a vibrant online community where vanlifers can connect, share experiences, and gain valuable insights into this unique lifestyle.
