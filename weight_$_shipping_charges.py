# Function to calculate shipping cost
def calculate_shipping_cost(weights, shipping_process):
    valid_shipping_processes = ['Express', 'Standard']
    express_rate = 11.80  # Cost per kg for Express shipping
    standard_rate = 6.80  # Cost per kg for Standard shipping

    if shipping_process not in valid_shipping_processes:
        return "Invalid shipping process. Valid options: Express, Standard"

    if not weights:
        return "Payload is empty."

    total_weight = 0
    total_cost = 0  
    highest_weight = 0  # Variable to track the highest weight
    highest_weight_index = -1  # Variable to store the index of the highest weight

    try:
        # Calculate total weight and shipping cost
        for i, item in enumerate(weights):
            weight = float(item["weight"]) * int(item["quantity"])
            # Modify this line to calculate item cost based on shipping process
            if weight > highest_weight:
                highest_weight = weight
                highest_weight_index = i

            total_weight += weight

        # Multiply the highest weight by 2
        new_highest_weight = highest_weight * 2

        # Add up the remaining weights to the new highest weight
        remaining_weight = total_weight - highest_weight
        new_highest_weight += remaining_weight

        # Replace the highest weight with the new calculated value
        if highest_weight_index != -1:
            weights[highest_weight_index]["weight"] = str(new_highest_weight)

        # Calculate the total shipping cost by multiplying the new highest weight by the shipping rate
        if shipping_process == 'Express':
            total_cost = new_highest_weight * express_rate
        elif shipping_process == 'Standard':
            total_cost = new_highest_weight * standard_rate

        return total_weight, total_cost, new_highest_weight

    except ValueError as e:
        return f"Error: {str(e)}. Please ensure weight and quantity are valid numbers."

# Example usage
weights = [
    {"weight": "1", "quantity": "2", "naira_price": "23800"},
    {"weight": "4", "quantity": "1", "naira_price": "3200"},
    {"weight": "3", "quantity": "5", "naira_price": "2100"}
]
shipping_process = 'Standard'

# Calculate and return the results
result = calculate_shipping_cost(weights, shipping_process)

if isinstance(result, tuple):
    new_highest_weight, shipping_cost, new_highest_weight = result
    formatted_shipping_cost = "₦{:,.2f}".format(float(shipping_cost))
    print("Total Weight:", new_highest_weight, "kg")
    print("Total Shipping Cost:", formatted_shipping_cost)
else:
    print(result)

#end