<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stylish Calculator</title>
    <style>
        /* Basic styling for the calculator with a purplish-peach theme */
        body, html {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f3e5f5; /* Light purple background */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            text-align: center;
        }

        h1 {
            color: #6a1b9a; /* Dark purple */
            margin-bottom: 20px;
        }

        .color-options {
            margin-bottom: 15px;
        }

        .color-button {
            width: 25px;
            height: 25px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            margin: 5px;
        }

        .calculator {
            background-color: #ba68c8; /* Medium purple */
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(106, 27, 154, 0.5); /* Glow effect */
        }

        #display {
            width: 100%;
            padding: 15px;
            margin-bottom: 10px;
            font-size: 1.5em;
            border: none;
            border-radius: 10px;
            background-color: #e1bee7; /* Light peach */
            color: #333;
            text-align: right;
            box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
        }

        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }

        button {
            padding: 15px;
            font-size: 1.2em;
            background-color: #7b1fa2; /* Darker purple */
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            box-shadow: 0 0 8px rgba(123, 31, 162, 0.7); /* Glow effect */
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        button:hover {
            background-color: #4a148c; /* Darker glow color */
            box-shadow: 0 0 12px rgba(74, 20, 140, 0.8); /* Intensified glow */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Stylish Calculator</h1>
        <div class="color-options">
            <button class="color-button" style="background-color: #ff6347;" onclick="changeColor('#ff6347')"></button>
            <button class="color-button" style="background-color: #32cd32;" onclick="changeColor('#32cd32')"></button>
            <button class="color-button" style="background-color: #ffb6c1;" onclick="changeColor('#ffb6c1')"></button>
            <button class="color-button" style="background-color: #1e90ff;" onclick="changeColor('#1e90ff')"></button>
            <button class="color-button" style="background-color: #ffdf00;" onclick="changeColor('#ffdf00')"></button>
        </div>
        <div class="calculator" id="calculator">
            <input type="text" id="display" disabled>
            <div class="buttons">
                <button onclick="clearDisplay()">C</button>
                <button onclick="deleteChar()">←</button>
                <button onclick="appendToDisplay('/')">/</button>
                <button onclick="appendToDisplay('*')">×</button>

                <button onclick="appendToDisplay('7')">7</button>
                <button onclick="appendToDisplay('8')">8</button>
                <button onclick="appendToDisplay('9')">9</button>
                <button onclick="appendToDisplay('-')">-</button>

                <button onclick="appendToDisplay('4')">4</button>
                <button onclick="appendToDisplay('5')">5</button>
                <button onclick="appendToDisplay('6')">6</button>
                <button onclick="appendToDisplay('+')">+</button>

                <button onclick="appendToDisplay('1')">1</button>
                <button onclick="appendToDisplay('2')">2</button>
                <button onclick="appendToDisplay('3')">3</button>
                <button onclick="calculateResult()">=</button>

                <button onclick="appendToDisplay('0')">0</button>
                <button onclick="appendToDisplay('.')">.</button>
            </div>
        </div>
    </div>

    <script>
        // Function to update the display with the clicked button's value
        function appendToDisplay(value) {
            document.getElementById('display').value += value;
        }

        // Function to clear the display
        function clearDisplay() {
            document.getElementById('display').value = '';
        }

        // Function to delete the last character from the display
        function deleteChar() {
            const display = document.getElementById('display');
            display.value = display.value.slice(0, -1);
        }

        // Function to calculate the result and display it
        function calculateResult() {
            try {
                const display = document.getElementById('display');
                display.value = eval(display.value);
            } catch (error) {
                alert('Invalid expression');
            }
        }

        // Function to change the theme color of the calculator
        function changeColor(color) {
            const calculator = document.getElementById('calculator');
            calculator.style.backgroundColor = color;
            calculator.style.boxShadow = `0 0 15px ${color}`;
        }
    </script>
</body>
</html>
