<h2 align="center"><u>Adhan-time-desktop-app</u></h2>

<p align="center">
<br>
    <img src="https://img.shields.io/badge/Author-NAZiha-magenta?style=flat-square">
    <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>
<h1>🕌 Adhan Time Desktop App</h1>
 
<p>
  <span class="badge">Python</span>
  <span class="badge">Tkinter</span>
  <span class="badge">Windows</span>
</p>
 
<p>A lightweight Windows desktop app that displays the five daily <strong>Adhan (prayer) times</strong> — Fajr, Dhuhr, Asr, Maghrib, and Isha — for any city in the world. Just type in a city name and get accurate, timezone-aware prayer times instantly.</p>
<img width="596" height="398" alt="screen shot" src="https://github.com/user-attachments/assets/be21afc6-17ff-4a53-a7a3-b6bd63623daa" />
<h2>Features</h2>
<ul>
  <li>🔍 <strong>City search</strong> — enter any city name to geolocate it and calculate local prayer times</li>
  <li>🕰️ <strong>Timezone-aware calculations</strong> — automatically detects the correct timezone for the searched location</li>
  <li>🌙 <strong>Five daily prayers</strong> — Fajr, Dhuhr, Asr, Maghrib, and Isha, displayed in a clean grid layout</li>
  <li>🖥️ <strong>Simple, distraction-free GUI</strong> — built with Tkinter, styled with a warm color palette</li>
  <li>⚡ <strong>Instant results</strong> — press Enter or click the search button to fetch times</li>
</ul>
 
<h2>▶️ How to Run</h2>
<ol>
  <li>Go to the <a href="https://github.com/httpsnaziha/Adhan-time-desktop-app/releases">Releases</a> page</li>
  <li>Download <code>Adhan.exe</code></li>
  <li>Double-click to run</li>
  <li>If Windows shows a security warning, click <strong>"More info"</strong> → <strong>"Run anyway"</strong></li>
</ol>
 
<blockquote>The app is packaged as a standalone Windows executable, so no Python installation is required to use it.</blockquote>
 
<h2>Running from Source</h2>
<p>If you'd rather run it directly from the Python source:</p>
 
<h3>Requirements</h3>
<ul>
  <li>Python 3.x</li>
  <li><a href="https://pypi.org/project/adhanpy/">adhanpy</a> — prayer time calculations</li>
  <li><a href="https://pypi.org/project/geopy/">geopy</a> — geocoding city names to coordinates</li>
  <li><a href="https://pypi.org/project/timezonefinder/">timezonefinder</a> — resolving timezone from coordinates</li>
  <li><a href="https://pypi.org/project/Pillow/">Pillow</a> — for loading the app icon</li>
</ul>
 
<pre><code>pip install adhanpy geopy timezonefinder pillow</code></pre>
 
<blockquote>Note: <code>tkinter</code> usually ships with Python by default. On Linux, you may need to install it separately (e.g. <code>sudo apt install python3-tk</code>).</blockquote>
 
<h3>Usage</h3>
<pre><code>git clone https://github.com/httpsnaziha/Adhan-time-desktop-app.git
cd Adhan-time-desktop-app
python Adhan.py</code></pre>
 
<p>Then type a city name into the search box and press <strong>Enter</strong> or click <strong>⌕</strong> to see the day's prayer times.</p>
 
<h2>How It Works</h2>
<ol>
  <li>The entered city name is geocoded via <strong>Nominatim</strong> (OpenStreetMap) to get its latitude/longitude.</li>
  <li><strong>TimezoneFinder</strong> determines the correct local timezone from those coordinates.</li>
  <li><strong>adhanpy</strong> calculates the day's prayer times using the <code>MOON_SIGHTING_COMMITTEE</code> calculation method.</li>
  <li>Results are displayed in the GUI, along with the resolved location address.</li>
</ol>
 
<h2>Project Structure</h2>
<pre><code>Adhan-time-desktop-app/
├── Adhan.py          # Main application (GUI + prayer time logic)
├── Adhan.spec        # PyInstaller spec file for building the .exe
├── app_icons/         # App icon and favicon assets
├── build/Adhan/        # PyInstaller build artifacts
├── dist/               # Compiled distributable output
└── favicon.ico          # Window icon</code></pre>
 
<h2>Notes</h2>
<ul>
  <li>Requires an internet connection, since geocoding relies on the Nominatim API.</li>
  <li>Prayer time calculation method is currently fixed to <strong>Moon Sighting Committee</strong>; other methods supported by <code>adhanpy</code> could be added as a setting in the future.</li>
  <li>Built and distributed for Windows via PyInstaller; other platforms would need to run it from source.</li>
</ul>
 
<h2>License</h2>
<p>No license specified yet — consider adding one (e.g. MIT) if you plan to share or accept contributions.</p>
 
</body>
</html>


<img width="596" height="398" alt="Capture d’écran 2026-07-21 133654" src="https://github.com/user-attachments/assets/4fc473d6-b56c-40d0-9611-45ef85c1bb4b" />
