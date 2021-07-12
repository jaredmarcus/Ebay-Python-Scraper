<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jaredmarcus/Ebay-Python-Scraper">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">eBay Scraper</h3>

  <p align="center">
    Python eBay scaper to pull relevant information from a listing. 
    <br />
    <a href="https://github.com/jaredmarcus/Ebay-Python-Scraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jaredmarcus/Ebay-Python-Scraper">View Demo</a>
    ·
    <a href="https://github.com/jaredmarcus/Ebay-Python-Scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/jaredmarcus/Ebay-Python-Scraper/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The main purpose of the project was to create a method of automating a post on eBay without using the API, but then came to the issue of getting captchas while reaching the login page. This is where I found that this method wouldn't be viable, but other developers, or people learning scraping might find this work of use. 

### Built With

* [Python 3.9.6](https://www.python.org/downloads/release/python-396/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure pip packages are up to date
* pip
  ```sh
  pip install --upgrade pip
  ```

### Installation

1. Clone the repo & place on your desktop
   ```sh
   git clone https://github.com/jaredmarcus/Ebay-Python-Scraper.git
   ```
2. Install requirements.txt
   ```sh
   pip install requirements.txt
   ```
3. Make Sure Repository Folder is placed on desktop or else the function won't run correctly (you'll have to edit some functions)



<!-- USAGE EXAMPLES -->
## Usage

The script works upon launch by asking for a link, you would just paste any eBay listing link (don't forget the www. part of the link). From there the script will open the link, and download relevant information. Title, Pictures, the Description, as well as the Price. 

<!-- ROADMAP -->
## Roadmap
Until I figure out a method on how to get past the captchas at the login screen, and automate a listing, since eBay has some logic developed to help sellers list their items (e.g. category for item derived from listings with a similar name) there won't be further updates for this repo. Feel free to fork and branch out to create further development of this project!
See the [open issues](https://github.com/jaredmarcus/Ebay-Python-Scraper/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jared Macias - [@twitter_handle](https://twitter.com/Frostyyy210) - jaredmarcus@icloud.com

Project Link: [https://github.com/jaredmarcus/Ebay-Python-Scraper](https://github.com/jaredmarcus/Ebay-Python-Scraper)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Stack Overflow explaining method to pull description for listing](https://stackoverflow.com/questions/63531321/is-it-possible-to-get-ebay-item-description-with-requests-and-beautifulsoup)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jaredmarcus/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/jaredmarcus/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jaredmarcus/repo.svg?style=for-the-badge
[forks-url]: https://github.com/jaredmarcus/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/jaredmarcus/repo.svg?style=for-the-badge
[stars-url]: https://github.com/jaredmarcus/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/jaredmarcus/repo.svg?style=for-the-badge
[issues-url]: https://github.com/jaredmarcus/repo/issues
[license-shield]: https://img.shields.io/github/license/jaredmarcus/repo.svg?style=for-the-badge
[license-url]: https://github.com/jaredmarcus/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jaredmarcus
