<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Segmentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: white; /* Changed background to white */
            color: black; /* Changed text color to black for better visibility */
            margin: 0;
            padding: 0;
        }
        .container {
            margin-top: 50px;
        }
        input {
            padding: 10px;
            width: 250px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            padding: 10px;
            background-color: blue;
            color: white;
            border: none;
            cursor: pointer;
            margin-left: 10px;
            border-radius: 5px;
        }
        .result {
            margin-top: 20px;
            font-size: 20px;
        }
        .segment {
            font-weight: bold;
            font-size: 24px;
            color: yellow;
        }
        .recommendation {
            font-size: 18px;
            margin-top: 10px;
            color: gray; /* Changed recommendation color to gray */
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>Customer Segmentation</h2>
        <input type="number" id="customerInput" placeholder="Enter Customer ID">
        <button onclick="analyzeCustomer()">Analyze</button>
        <div class="result" id="result"></div>
    </div>

    <script>
        const dataset = [
            { "CustomerID": 12405, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12406, "Customer_Segment": "Promising" },
            { "CustomerID": 12407, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12408, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12409, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12410, "Customer_Segment": "Lost Lowest" },
            { "CustomerID": 12411, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12412, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12414, "Customer_Segment": "About To Sleep" },
            { "CustomerID": 12415, "Customer_Segment": "Loyal Customers" },
            { "CustomerID": 12417, "Customer_Segment": "Loyal Customers" },
            { "CustomerID": 12418, "Customer_Segment": "Loyal Customers" },
            { "CustomerID": 12419, "Customer_Segment": "New Customers" },
            { "CustomerID": 12421, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12422, "Customer_Segment": "Promising" },
            { "CustomerID": 12423, "Customer_Segment": "Potential Loyalist" },
            { "CustomerID": 12424, "Customer_Segment": "Promising" }
        ];

        function analyzeCustomer() {
            let customerID = document.getElementById("customerInput").value.trim();
            let resultDiv = document.getElementById("result");

            let customer = dataset.find(c => c.CustomerID == customerID);

            if (customer) {
                let segment = customer.Customer_Segment;
                let recommendation = getRecommendation(segment);

                resultDiv.innerHTML = `<p class="segment">${segment}</p>
                                            <p class="recommendation"><strong>Recommended action:</strong> ${recommendation}</p>`;
            } else {
                resultDiv.innerHTML = `<p class="segment">Unknown Customer</p>
                                            <p class="recommendation"><strong>Recommended action:</strong> No data available. Please ensure the Customer ID is correct.</p>`;
            }
        }

        function getRecommendation(segment) {
            const recommendations = {
                "Best Customer": "These are your top customers who frequently purchase from you. Maintain a strong relationship with them by offering exclusive benefits such as VIP discounts, early access to new products, and personalized experiences. Keep them engaged through loyalty programs and premium customer service.",
                "Potential Loyalist": "This customer is showing signs of loyalty but needs a little encouragement. Consider sending them personalized discount offers, engaging them through email marketing, and providing exceptional service to turn them into a long-term loyal customer.",
                "Promising": "This customer has potential but is not fully engaged yet. Provide targeted promotions, such as first-time purchase discounts or bundled deals, to increase their interest and encourage repeat purchases. Sending educational content about your products can also be helpful.",
                "Loyal Customers": "These customers consistently choose your brand. Reward them with exclusive membership perks, birthday discounts, and surprise gifts. Encourage them to refer others by introducing referral programs with benefits for both them and their friends.",
                "New Customers": "Welcome this customer with a great first experience! Offer a special welcome discount, provide helpful onboarding information, and send follow-up emails with recommendations based on their first purchase. Excellent customer service at this stage can turn them into loyal buyers.",
                "About To Sleep": "This customer has not made a purchase in a while and is at risk of churning. Re-engage them by sending special limited-time offers, reminders of past purchases, and personalized messages that show you value their business.",
                "Lost Lowest": "This customer is highly inactive and has a low purchase history. Instead of spending too much on re-engagement, use minimal marketing efforts like occasional newsletters or discount emails to try to bring them back, but focus your main resources on high-value customers."
            };
            return recommendations[segment] || "No specific action recommended.";
        }
    </script>

</body>
</html>