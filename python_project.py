from flask import Flask, render_template_string

app = Flask(__name__)

def page(title, content):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>

        <style>
            body {{
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
            }}

            /* NAVBAR */
            nav {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 40px;
                background: rgba(0,0,0,0.6);
                backdrop-filter: blur(10px);
                position: sticky;
                top: 0;
            }}

            .logo {{
                display: flex;
                align-items: center;
                gap: 10px;
            }}

            nav ul {{
                list-style: none;
                display: flex;
                gap: 25px;
            }}

            nav a {{
                color: white;
                text-decoration: none;
                transition: 0.3s;
                font-weight: 500;
            }}

            nav a:hover {{
                color: #00d4ff;
            }}

            /* HERO */
            .hero {{
                text-align: center;
                padding: 100px 20px;
                animation: fadeIn 1.5s ease-in;
            }}

            .hero h1 {{
                font-size: 45px;
            }}

            .hero p {{
                color: #ccc;
            }}

            /* CARDS */
            .cards {{
               display: flex;
               flex-wrap: wrap;
               justify-content: center;
               gap: 30px;
               margin-top: 50px;
            }}

            
           

           .card {{
              background: rgba(255,255,255,0.1);
              padding: 20px;
              width: 260px;
              height: 100px;
              border-radius: 15px;
              text-align: center;
              font-size: 16px;
              display: flex;
              align-items: center;
              justify-content: center;
              word-wrap: break-word;
          }}   

          .card:hover {{
             transform: scale(1.1);
             background: rgba(255,255,255,0.2);
          }}

         .card a {{
            color: white;
            text-decoration: none;
            display: block;
          }}

            /* FOOTER */
            footer {{
                text-align: center;
                padding: 30px;
                border-top: 1px solid #aaa;
                margin-top: 40px;
            }}

            /* ANIMATION */
            @keyframes fadeIn {{
                from {{opacity:0; transform:translateY(20px);}}
                to {{opacity:1; transform:translateY(0);}}
            }}
        </style>
    </head>

    <body>

    <!-- NAVBAR -->
    <nav>
        <div class="logo">
            <!-- Amazon "a" icon -->
            <img src="/static/amazon.jpeg" height="80">
            <h3>Amazon Project</h3>
        </div>

        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/dataset">Dataset</a></li>
            <li><a href="/correlation">Correlation</a></li>
            <li><a href="/regression">Predictive Data Analysis</a></li>
            <li><a href="/loyal">Behavioral Segmentation</a></li>
            <li><a href="/powerbi">Exploratory Data Analysis</a></li>
            <li><a href="/conclusion">Conclusion</a></li>
            <li><a href="/credits">Credits</a></li>
        </ul>
    </nav>

    <!-- HERO -->
    <div class="hero">
        <h1>{title}</h1>
        <p>{content}</p>
    </div>

    <!-- CARDS -->
    <div class="cards">
    <div class="card"><a href="/dataset" style="color:white;">Dataset</a></div>
    <div class="card"><a href="/correlation" style="color:white;">Correlation</a></div>
    <div class="card"><a href="/regression" style="color:white;">Predictive Data Analysis</a></div>
    <div class="card"><a href="/loyal" style="color:white;">Behavioral Segmentation</a></div>
    <div class="card"><a href="/powerbi" style="color:white;">Exploratory Data Analysis</a></div>
    <div class="card"><a href="/conclusion" style="color:white;">Conclusion</a></div
    </div>

    <!-- FOOTER WITH YOUR PDEU LOGO -->
    
    <footer>
        <div style="margin-top:20px;">
            <img src="/static/pdeu.png" height="80" 
                 style="background:white; padding:10px; border-radius:12px;">
        </div>
        <p>Pandit Deendayal Energy University, Gandhinagar</p>
    </footer>

    </body>
    </html>
    """
@app.route("/")
def home():
    return """
    <html>
    <head>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
            }

            /* NAVBAR */
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px 40px;
                background: rgba(0,0,0,0.5);
            }

            .logo {
                display: flex;
                align-items: center;
                gap: 10px;
            }

            .logo img {
                height: 40px;
            }

            ul {
                list-style: none;
                display: flex;
                gap: 20px;
            }

            ul li a {
                color: white;
                text-decoration: none;
                font-size: 16px;
            }

            /* HERO */
            .hero {
                margin-top: 50px;
            }

            .hero h1 {
                font-size: 40px;
            }

            .hero p {
                font-size: 18px;
                margin-top: 10px;
            }

            /* CARDS */
            .cards {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 30px;
                margin-top: 50px;
            }

            .card {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                width: 260px;
                height: 100px;
                border-radius: 15px;
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                color: white;
                font-size: 16px;
                word-wrap: break-word;
            }

            .card:hover {
                background: rgba(255,255,255,0.2);
            }

            /* FOOTER */
            footer {
                text-align: center;
                margin-top: 80px;
                padding: 20px;
            }

            footer img {
                display: block;
                margin: 0 auto;
                margin-bottom: 10px;
                height: 80px;
            }

            footer p {
                font-size: 16px;
            }
        </style>
    </head>

    <body>

        <!-- NAVBAR -->
        <nav>
            <div class="logo">
                <img src="/static/amazon.jpeg">
                <h3>Amazon Project</h3>
            </div>

            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/dataset">Dataset</a></li>
                <li><a href="/correlation">Correlation</a></li>
                <li><a href="/regression">Predictive Data Analysis</a></li>
                <li><a href="/loyal">Behavioral Segmentation</a></li>
                <li><a href="/powerbi">Exploratory Data Analysis</a></li>
                <li><a href="/conclusion">Conclusion</a></li>
                <li><a href="/credits">Credits</a></li>
            </ul>
        </nav>

        <!-- HERO -->
        <div class="hero">
            <h1>Amazon Dataset Analysis</h1>
            <p>A Data Science Project with Apple-style UI</p>
        </div>

        <!-- BUTTONS -->
        <div class="cards">
            <a href="/dataset" class="card">Dataset</a>
            <a href="/correlation" class="card">Correlation</a>
            <a href="/regression" class="card">Predictive Data Analysis</a>
            <a href="/loyal" class="card">Behavioral Segmentation</a>
            <a href="/powerbi" class="card">Exploratory Data Analysis</a>
            <a href="/conclusion" class="card">Conclusion</a>
        </div>

        <!-- FOOTER -->
        <footer>
            <img src="/static/pdeu.png">
            <p>Pandit Deendayal Energy University, Gandhinagar</p>
        </footer>

    </body>
    </html>
    """

@app.route("/dataset")
def dataset():
    return """
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: Arial;
                text-align: center;
                color: white;
                margin-top: 50px;
            }

            .btn {
                display: block;
                width: 400px;
                margin: 20px auto;
                padding: 15px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                background: rgba(255,255,255,0.2);
            }

            iframe {
                width: 90%;
                height: 500px;
                border: none;
                display: none;
                margin: auto;
            }
        </style>
    </head>

    <body>

        <h1>Dataset</h1>

        <a class="btn" href="https://www.kaggle.com/datasets/anandshaw2001/amazon-sales-dataset" target="_blank">
            📊 View Dataset on Kaggle
        </a>

        <a class="btn" href="/dataset_view">
           📄 View Excel
        </a>

        <iframe id="frame"></iframe>

        <script>
            function loadExcel() {
                document.getElementById("frame").style.display = "block";
                document.getElementById("frame").src = "/dataset_view";
            }
        </script>

    </body>
    </html>
    """
@app.route("/dataset_view")
def dataset_view():
    import pandas as pd
    import os

    file_path = os.path.join("static", "amazon1.csv")

    df = pd.read_csv(file_path, nrows=20)
    return df.to_html(index=False)   

@app.route("/correlation")
def correlation():
    return """
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: Arial;
                text-align: center;
                color: white;
                margin-top: 60px;
            }

            .btn {
                display: block;
                width: 400px;
                margin: 20px auto;
                padding: 15px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                background: rgba(255,255,255,0.2);
                cursor: pointer;
            }

            .btn:hover {
                background: rgba(255,255,255,0.4);
            }

            .section {
                display: none;
                margin-top: 30px;
            }

            .slide {
                display: none;
                width: 100%;
                height: 80vh;
                object-fit: contain;
            }

            .nav-btn {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                background: rgba(0,0,0,0.5);
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 20px;
                cursor: pointer;
                border-radius: 10px;
            }

            .prev { left: 20px; }
            .next { right: 20px; }

            .content {
                max-width: 900px;
                margin: auto;
                text-align: left;
                font-size: 18px;
                line-height: 1.8;
                padding: 20px;
                white-space: pre-line; /* VERY IMPORTANT */
            }
        </style>
    </head>

    <body>

        <h1>Correlation Analysis</h1>

        <!-- BUTTONS -->
        <div class="btn" onclick="showSection('code')">📸 Code & Output</div>
        <div class="btn" onclick="showSection('text')">📘 Explanation</div>

        <!-- CODE SECTION -->
        <div id="code" class="section">
            <img class="slide" src="/static/corr1.jpeg">
            <img class="slide" src="/static/corr2.jpeg">
            <img class="slide" src="/static/corr3.jpeg">
            <img class="slide" src="/static/corr4.jpeg">

            <button class="nav-btn prev" onclick="changeSlide(-1)">❮</button>
            <button class="nav-btn next" onclick="changeSlide(1)">❯</button>
        </div>

        <!-- EXACT TEXT -->
        <div id="text" class="section content">

1. Purpose of the Model (Correlation Analysis)
The goal of our model is:
* To measure the strength and direction of relationships between variables:
1. Purchase (Total Amount spent)
2. Discount
3. Quantity

In simple terms:
“We are trying to understand how these variables move together — whether increasing one affects the others.”

2. Understanding Correlation Values
Correlation ranges from -1 to +1:
+1 → Strong positive relationship
0 → No relationship
-1 → Strong negative relationship

#Correlation Values ( Interpretation)

1. Purchase vs Quantity → +0.5949
Moderate Positive Correlation
Meaning:
As Quantity increases, Purchase amount also increases
This is logical (more items → more total cost)

“Customers buying more items tend to spend more overall, showing a moderate positive relationship.”

2. Purchase vs Discount → -0.1081
Weak Negative Correlation
Meaning:
Slight tendency: higher discounts → slightly lower purchase amount
BUT the relationship is very weak

Important insight:
Discount is NOT strongly influencing total spending.

“Discount has a negligible negative impact on total purchase value.”

3. Discount vs Quantity → -0.0004 (≈ 0)
No Correlation

Meaning:
Discount does not affect how many items people buy.

#Heatmap Insight (Visual Explanation)
• Bright Yellow (1.0) → Perfect correlation (same variable)
• Green (~0.6) → Moderate positive (Purchase–Quantity)
• Dark Purple (~0) → No relation (Discount–Quantity)
• Slight Purple (~-0.1) → Weak negative (Purchase–Discount)

5. To Conclude :-

Key Insights:
• Quantity is the main driver of purchase value
• Discounts have minimal impact on buying behavior
• Customer spending depends more on how much they buy, not discounts.

--------------------------------------------------

• Revenue mainly depends on price and purchase volume.
• Discounts significantly reduce profit margins.
• Tax has a positive but moderate impact.
• Shipping cost is not a major revenue driver.
• Pricing strategy and Quantity are crucial for revenue.
• More items purchased = much higher total revenue.
• Even small increases in discount sharply reduce total amount.

        </div>

        <script>
            function showSection(id) {
                document.getElementById("code").style.display = "none";
                document.getElementById("text").style.display = "none";

                document.getElementById(id).style.display = "block";

                if(id === "code") showSlide(0);
            }

            let index = 0;

            function showSlide(i) {
                let slides = document.getElementsByClassName("slide");

                if (i >= slides.length) index = 0;
                if (i < 0) index = slides.length - 1;

                for (let j = 0; j < slides.length; j++) {
                    slides[j].style.display = "none";
                }

                slides[index].style.display = "block";
            }

            function changeSlide(n) {
                index += n;
                showSlide(index);
            }
        </script>

    </body>
    </html>
    """

@app.route("/regression")
def regression():
    return """
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: Arial;
                text-align: center;
                color: white;
                margin-top: 80px;
            }

            .btn {
                display: block;
                width: 400px;
                margin: 20px auto;
                padding: 15px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                background: rgba(255,255,255,0.2);
            }

            .btn:hover {
                background: rgba(255,255,255,0.4);
            }

            .content {
                max-width: 900px;
                margin: 40px auto;
                font-size: 18px;
                line-height: 1.8;
                text-align: left;
            }

            h1 {
                margin-bottom: 30px;
            }

            h2 {
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    </head>

    <body>

        <h1>Regression Analysis</h1>

        <!-- BUTTONS -->
        <a class="btn" href="https://colab.research.google.com/drive/1LA79AXTHOeJ6wqpOs5FFjvOZfSIxCSDt?usp=drive-dynamite#scrollTo=_62Fy49ho5Yl" target="_blank">
            📊 Linear Regression Notebook
        </a>

        <a class="btn" href="https://colab.research.google.com/drive/1Yb0rXU654GU05kSd_MNcOqZ_T5U9kJFR?usp=drive-dynamite" target="_blank">
            📈 Predictive Regression Notebook
        </a>

        <!-- SUMMARY -->
        <div class="content">

            <h2>Regression Analysis Summary</h2>

            <p>
            This section presents the implementation of linear regression models to analyze and predict relationships within the dataset. 
            The models are built using Python and executed in Google Colab notebooks.
            </p>

            <p>
            The first notebook focuses on understanding the basic concept of linear regression, where the relationship between independent 
            and dependent variables is established using a best-fit line. It helps in identifying how changes in input variables affect the output.
            </p>

            <p>
            The second notebook extends this concept to predictive analysis, where the trained regression model is used to forecast future values. 
            This allows better decision-making based on data trends.
            </p>

            <p>
            Overall, regression analysis helps in identifying patterns, understanding variable relationships, and making data-driven predictions, 
            which are essential for business insights and strategic planning.
            </p>

        </div>

    </body>
    </html>
    """

@app.route("/loyal")
def loyal():
    return """
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: Arial;
                text-align: center;
                color: white;
                margin-top: 60px;
            }

            .btn {
                display: block;
                width: 400px;
                margin: 20px auto;
                padding: 15px;
                font-size: 18px;
                border-radius: 10px;
                text-decoration: none;
                color: white;
                background: rgba(255,255,255,0.2);
                cursor: pointer;
            }

            .btn:hover {
                background: rgba(255,255,255,0.4);
            }

            .section {
                display: none;
                margin-top: 30px;
            }

            .slide {
                display: none;
                width: 100%;
                height: 80vh;
                object-fit: contain;
            }

            .nav-btn {
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                background: rgba(0,0,0,0.5);
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 20px;
                cursor: pointer;
                border-radius: 10px;
            }

            .prev { left: 20px; }
            .next { right: 20px; }

            .content {
                max-width: 900px;
                margin: auto;
                text-align: left;
                font-size: 18px;
                line-height: 1.8;
                padding: 20px;
                white-space: pre-line;
            }
        </style>
    </head>

    <body>

        <h1>Behavioral Segmentation</h1>

        <!-- BUTTONS -->
        <div class="btn" onclick="showSection('code')">📸 Code & Output</div>
        <div class="btn" onclick="showSection('text')">📘 Explanation</div>

        <!-- CODE SECTION -->
        <div id="code" class="section">
            <img class="slide" src="/static/loyal1.jpeg">
            <img class="slide" src="/static/loyal2.jpeg">
            <img class="slide" src="/static/loyal3.jpeg">
            <img class="slide" src="/static/loyal4.jpeg">
            <img class="slide" src="/static/loyal5.jpeg">
            <img class="slide" src="/static/loyal6.jpeg">

            <button class="nav-btn prev" onclick="changeSlide(-1)">❮</button>
            <button class="nav-btn next" onclick="changeSlide(1)">❯</button>
        </div>

        <!-- EXACT TEXT -->
        <div id="text" class="section content">

This project uses pandas to analyze customer order data from an Excel file. The data is first cleaned and standardized to remove inconsistencies. Then, customers are grouped based on their IDs to calculate the total number of orders placed. The main objective is to identify loyal customers by filtering those who have placed five or more orders. The final output is displayed in a well-formatted and visually styled table for better understanding and presentation.

⸻

🔑 Key Points
• ✔ Data is loaded from an Excel file using pandas
• ✔ Column names are cleaned (removal of extra spaces)
• ✔ Customer ID and Name fields are standardized
• ✔ Data is grouped by customer to count total orders
• ✔ Loyal customers (≥ 5 orders) are filtered
• ✔ Results are sorted in descending order of orders
• ✔ Diagnostic checks are performed (rows, columns, max orders)
• ✔ Final table is styled with formatting and color gradients
• ✔ Helps in identifying high-value and frequent customers

        </div>

        <script>
            function showSection(id) {
                document.getElementById("code").style.display = "none";
                document.getElementById("text").style.display = "none";

                document.getElementById(id).style.display = "block";

                if(id === "code") showSlide(0);
            }

            let index = 0;

            function showSlide(i) {
                let slides = document.getElementsByClassName("slide");

                if (i >= slides.length) index = 0;
                if (i < 0) index = slides.length - 1;

                for (let j = 0; j < slides.length; j++) {
                    slides[j].style.display = "none";
                }

                slides[index].style.display = "block";
            }

            function changeSlide(n) {
                index += n;
                showSlide(index);
            }
        </script>

    </body>
    </html>
    """
   
 

@app.route("/powerbi")
def powerbi():
    return """
    <html>
    <head>
        <style>
            body {
                margin: 0;
                background: black;
                color: white;
                font-family: Arial;
            }

            /* IMAGE */
            .dashboard-img {
                width: 100%;
                height: 80vh;
                object-fit: contain;
                display: block;
            }

            /* TEXT SECTION */
            .content {
                padding: 30px;
                max-width: 1000px;
                margin: auto;
                line-height: 1.8;
                font-size: 18px;
            }

            h1 {
                text-align: center;
                margin-top: 20px;
            }

            .point {
                margin-bottom: 20px;
            }
        </style>
    </head>

    <body>

        <h1>Power BI Dashboard Analysis</h1>

        <!-- IMAGE -->
        <img class="dashboard-img" src="/static/powerbi.jpeg">

        <!-- TEXT -->
        <div class="content">

            <p>This dashboard provides a comprehensive view of sales, tax, discounts, and customer behavior across countries, categories, and payment methods.</p>

            <div class="point"><b>Country-Level Performance:</b><br>
            Canada is the top-performing market, making it a key focus area for business growth.</div>

            <div class="point"><b>Payment Method Distribution:</b><br>
            Customers prefer cashless transactions, indicating a strong digital adoption trend.</div>

            <div class="point"><b>Discount Analysis by Country:</b><br>
            Heavy discounting in the US may be driving sales or reducing profit margins. This needs optimization.</div>

            <div class="point"><b>Customer-Level Discount Behavior:</b><br>
            Discounts are not evenly distributed. Likely targeted toward high-value or frequent customers.</div>

            <div class="point"><b>Category Insights:</b><br>
            Product categories are performing consistently, with no major outliers.</div>

            <div class="point"><b>State-Level Discount Distribution:</b><br>
            No single state dominates → indicates broad geographic customer base.</div>

        </div>

    </body>
    </html>
    """
@app.route("/credits")
def credits():
    return """
    <html>
    <head>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                color: white;
                overflow: hidden;
            }

            /* FULL BACKGROUND IMAGE */
            .bg {
                position: fixed;
                width: 100%;
                height: 100%;
                object-fit: cover;
                z-index: -1;
            }

            /* BOTTOM RIGHT BOX */
            .credits-box {
                position: absolute;
                bottom: 30px;
                right: 30px;
                text-align: right;

                background: rgba(0, 0, 0, 0.5);
                padding: 20px;
                border-radius: 15px;
                backdrop-filter: blur(10px);

                animation: fadeIn 2s ease-in;
            }

            /* TITLE */
            .title {
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 10px;
                text-shadow: 0 0 10px white;
            }

            /* NAMES */
            .names {
                font-size: 18px;
                line-height: 2;
                text-shadow: 0 0 8px white;
                animation: slideUp 2s ease-in;
            }

            /* FADE IN ANIMATION */
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* SLIDE UP EFFECT */
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(50px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>

    <body>

        <!-- BACKGROUND IMAGE -->
        <img src="/static/thank_you.jpg" class="bg">

        <!-- TEXT BOX -->
        <div class="credits-box">
            <div class="title">Made by:</div>

            <div class="names">
                Anayaa Raisurana (25BSD004) <br>
                Helly Thakkar (25BSD015) <br>
                Joel Paul Santosh (25BSD020) <br>
                Nishtha Prajapati (25BSD036) <br>
                Riya Shukla (25BSD048)
            </div>
        </div>

    </body>
    </html>
    """

@app.route("/conclusion")
def conclusion():
    return """
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: Arial;
                color: white;
                padding: 40px;
                line-height: 1.8;
            }

            h1 {
                text-align: center;
                margin-bottom: 30px;
            }

            .content {
                max-width: 1000px;
                margin: auto;
                font-size: 18px;
                white-space: pre-line; /* IMPORTANT for exact formatting */
            }
        </style>
    </head>

    <body>

        <h1>Conclusion</h1>

        <div class="content">

Based on the analysis of the Amazon e-commerce dataset from 2020–2024, it is observed that purchase value is mainly influenced by the quantity of items bought. The correlation analysis and graphical results indicate a moderate positive relationship between quantity and total purchase amount, showing that customers who buy more items contribute significantly to overall revenue. On the other hand, discount has a very weak relationship with both quantity and purchase value, suggesting that discounts do not strongly influence customer buying behaviour.

The distribution plots further show that most transactions are of low to moderate value, with only a few high-value purchases. Shipping cost appears relatively consistent across orders, while tax increases proportionally with total purchase amount. These findings indicate that revenue growth is largely driven by purchase volume rather than promotional offers.

Additionally, the weak impact of discounts suggests the presence of loyal customers who continue purchasing regardless of price reductions. Such repeat buyers tend to purchase more frequently and in higher quantities, thereby contributing substantially to sales performance. This highlights the importance of customer retention strategies.

Overall, the study concludes that increasing customer loyalty and encouraging higher purchase quantities are more effective for revenue growth than relying heavily on discounts. The results also align with sustainable consumption principles, as businesses can focus on responsible sales strategies rather than excessive promotional tactics.

        </div>

    </body>
    </html>
    """          

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
