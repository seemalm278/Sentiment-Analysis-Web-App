async function predictSentiment() {

    const text = document.getElementById("textInput").value;
    const result = document.getElementById("result");
    result.className = "result-box";

    // Check for empty input
    if (text.trim() === "") {
        result.innerHTML = "⚠️ Please enter some text.";
        result.style.color = "orange";
        return;
    }

    // Loading message
    result.innerHTML = "⏳ Analyzing sentiment...";
    result.style.color = "#007bff";

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        if (data.prediction === "Positive") {
           result.innerHTML = "😊 Positive";
result.className = "result-box result-positive";
        }
        else if (data.prediction === "Negative") {
            result.innerHTML = "😞 Negative";
result.className = "result-box result-negative";
        }
        else {
            result.innerHTML = "😐 Neutral";
result.className = "result-box result-neutral";
        }

    }
    catch (error) {

        console.error(error);

        result.innerHTML = "❌ Unable to connect to the API.";
        result.className = "result-box result-negative";

    }

}
function clearText() {

    document.getElementById("textInput").value = "";

    const result = document.getElementById("result");
    result.innerHTML = "";
    result.style.color = "black";

}