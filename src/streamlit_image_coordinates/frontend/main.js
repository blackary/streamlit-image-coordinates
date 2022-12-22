// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
  Streamlit.setComponentValue(value)
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
  // Only run the render code the first time the component is loaded.
  if (!window.rendered) {
    // You most likely want to get the data passed in like this
    let {src, height, width} = event.detail.args

    const img = document.getElementById("image")
    img.src = src

    img.onload = () => {

      if (!width && !height) {
        width = img.naturalWidth
        height = img.naturalHeight
      }
      else if (!height) {
        height = width * img.naturalHeight / img.naturalWidth
      }
      else if (!width) {
        width = height * img.naturalWidth / img.naturalHeight
      }

      img.width = width
      img.height = height

      Streamlit.setFrameHeight(height)

      // When image is clicked, send the coordinates to Python through sendValue

      img.addEventListener("click", (e) => {
        const {offsetX, offsetY} = e
        sendValue({x: offsetX, y: offsetY})
      })

      // You'll most likely want to pass some data back to Python like this
      // sendValue({output1: "foo", output2: "bar"})
      window.rendered = true
    }
  }
}

// Render the component whenever python send a "render event"
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// Tell Streamlit that the component is ready to receive events
Streamlit.setComponentReady()
// Render with the correct height, if this is a fixed-height component
// Streamlit.setFrameHeight(100)
