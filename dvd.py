import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DVD Bounce", layout="centered")

st.title("📀 Streamlit DVD Bounce")
st.write("A smooth animation using injected JavaScript.")

# HTML/JS for the animation
dvd_html = """
<div id="container" style="width: 100%; height: 400px; background: black; position: relative; overflow: hidden; border-radius: 10px;">
    <div id="logo" style="width: 80px; height: 40px; background: #00ff00; position: absolute; display: flex; align-items: center; justify-content: center; color: white; font-family: sans-serif; font-weight: bold; border-radius: 4px;">
        DVD
    </div>
</div>

<script>
    const container = document.getElementById('container');
    const logo = document.getElementById('logo');
    
    let x = 0;
    let y = 0;
    let xSpeed = 2;
    let ySpeed = 2;

    function animate() {
        const cWidth = container.clientWidth;
        const cHeight = container.clientHeight;
        const lWidth = logo.offsetWidth;
        const lHeight = logo.offsetHeight;

        x += xSpeed;
        y += ySpeed;

        if (x + lWidth >= cWidth || x <= 0) {
            xSpeed *= -1;
            logo.style.backgroundColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        }
        if (y + lHeight >= cHeight || y <= 0) {
            ySpeed *= -1;
            logo.style.backgroundColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        }

        logo.style.left = x + 'px';
        logo.style.top = y + 'px';

        requestAnimationFrame(animate);
    }
    animate();
</script>
"""

# Render the component
components.html(dvd_html, height=450)

st.success("The logo changes color every time it hits a wall!")

