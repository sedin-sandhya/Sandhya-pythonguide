"""
Mobile Recharge Plan Selector: 

Ask user for their budget and usage preference (calls / data / both). 
Recommend the best recharge plan from 3 options 
and show what they save vs the next plan. 

Enter your budget (₹): 300 
Preference (calls/data/both): data 
--- 
Best Plan: ₹239 — 1.5GB/day, 28 days 
You save ₹61 vs the ₹299 plan. 
Extra data vs ₹199 plan: +0.5GB/day 
"""

plans = {
    "calls": [
        {
            "name": "Basic",
            "price": 199,
            "calls": "Unlimited",
            "data": "100MB/day",
            "validity": 28
        },
        {
            "name": "Mid",
            "price": 239,
            "calls": "Unlimited",
            "data": "300MB/day",
            "validity": 28
        },
        {
            "name": "Premium",
            "price": 299,
            "calls": "Unlimited",
            "data": "500MB/day",
            "validity": 56
        }
    ],

    "data": [
        {
            "name": "Basic",
            "price": 199,
            "data": "1GB/day",
            "calls": "100 mins/day",
            "validity": 28
        },
        {
            "name": "Mid",
            "price": 239,
            "data": "1.5GB/day",
            "calls": "Unlimited",
            "validity": 28
        },
        {
            "name": "Premium",
            "price": 299,
            "data": "2GB/day",
            "calls": "Unlimited",
            "validity": 56
        }
    ],

    "both": [
        {
            "name": "Basic",
            "price": 199,
            "data": "1GB/day",
            "calls": "Unlimited",
            "sms": "100/day",
            "validity": 28
        },
        {
            "name": "Mid",
            "price": 239,
            "data": "1.5GB/day",
            "calls": "Unlimited",
            "sms": "100/day",
            "validity": 28
        },
        {
            "name": "Premium",
            "price": 299,
            "data": "2GB/day",
            "calls": "Unlimited",
            "sms": "100/day",
            "validity": 56
        }
    ]
}

budget = int(input("Enter your budget in Rs: "))
preference = input("Preference (calls/data/both): ") 
selected_plans = plans[preference]
best_plan = {}

affordable = []
for plan in selected_plans:
    if(plan["price"] <= budget):
        affordable.append(plan)

if(len(affordable) == 0):
    print("Sorry, No plans available under the budget")
else:
    if preference != "calls":
        best_plan = affordable[-1]
    else:
        best_plan = affordable[0]

    index = selected_plans.index(best_plan)
    if preference == "data":
        print(
                f"Best Plan: ₹{best_plan['price']} — "
                f"{best_plan['data']}, "
                f"{best_plan['validity']} days, "
                f"{best_plan['calls']} calls"
            )
    elif preference == "calls":
        print(
                f"Best Plan: ₹{best_plan['price']} - "
                f"{best_plan['calls']} calls, "
                f"{best_plan['data']}, "
                f"{best_plan['validity']} days"
        )
    else :
        print(
            f"Best Plan: ₹{best_plan['price']} — "
            f"{best_plan['data']}, "
            f"{best_plan['calls']} calls, "
            f"{best_plan['sms']} SMS/day, "
            f"{best_plan['validity']} days"
        )

    if len(selected_plans)-1 == index:
        print("You save ₹0 (this is the top plan!)")
    else:
        next_plan = selected_plans[index+1]
        print(
            f"You save ₹{next_plan['price'] - best_plan['price']} "
            f"vs the ₹{next_plan['price']} plan (out of budget)"
        )
    
    if index == 0:
        print("No lower plan to compare against.")
    else:
        lower_plan = selected_plans[index - 1]

        if preference in ("data", "both"):
            extra_data = (float(best_plan['data'][:-6]) - 
            float(lower_plan['data'][:-6]))

            print(
                    f"Extra data vs ₹{lower_plan['price']} plan: "
                    f"+{extra_data}GB/day"
            )
        

