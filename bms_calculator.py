"""
BMI (Body Mass Index) Calculator
==================================

A comprehensive tool to calculate Body Mass Index with detailed health insights.

Body Mass Index (BMI) is a measure that uses your height and weight to work out 
if your weight is healthy. BMI is a useful measurement for most people over 18 years old.

Features:
- Supports both metric (kg, meters) and imperial (lbs, inches) units
- WHO standard BMI categorization
- Health recommendations based on BMI category
- Educational information about BMI and health

Note: BMI may not be accurate for athletes, pregnant women, elderly, or children.
Always consult healthcare professionals for personalized medical advice.

hacktoberfest
hacktoberfest-accepted
hacktoberfest2025
"""

def calculate_bmi(weight, height, unit_system='metric'):
    """
    Calculate BMI based on weight and height
    
    Args:
        weight (float): Weight in kilograms (metric) or pounds (imperial)
        height (float): Height in meters (metric) or inches (imperial)
        unit_system (str): 'metric' or 'imperial'
    
    Returns:
        float: BMI value
    """
    try:
        if unit_system == 'metric':
            # BMI = weight(kg) / height(m)^2
            bmi = weight / (height ** 2)
        elif unit_system == 'imperial':
            # BMI = (weight(lbs) / height(in)^2) * 703
            bmi = (weight / (height ** 2)) * 703
        else:
            raise ValueError("Unit system must be 'metric' or 'imperial'")
        
        return round(bmi, 2)
    except ZeroDivisionError:
        raise ValueError("Height cannot be zero")

def get_bmi_category(bmi):
    """
    Determine BMI category based on WHO standards
    
    Args:
        bmi (float): BMI value
    
    Returns:
        str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_health_recommendation(category):
    """
    Provide basic health recommendations based on BMI category
    
    Args:
        category (str): BMI category
    
    Returns:
        str: Health recommendation
    """
    recommendations = {
        "Underweight": "Consider consulting a nutritionist to develop a healthy weight gain plan.",
        "Normal weight": "Maintain your current healthy lifestyle with balanced diet and regular exercise.",
        "Overweight": "Focus on balanced nutrition and regular physical activity. Consider consulting a healthcare provider.",
        "Obese": "Consult with healthcare professionals for a comprehensive weight management plan."
    }
    return recommendations.get(category, "Consult a healthcare provider for personalized advice.")

def display_bmi_result(bmi, category, recommendation):
    """
    Display BMI results in a formatted way
    
    Args:
        bmi (float): BMI value
        category (str): BMI category
        recommendation (str): Health recommendation
    """
    print("\n" + "="*50)
    print("BMI CALCULATOR RESULTS")
    print("="*50)
    print(f"Your BMI: {bmi}")
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")
    print("="*50)

def get_user_input():
    """
    Get user input for weight, height, and unit system with clear prompts
    
    Returns:
        tuple: (weight, height, unit_system)
    """
    print("\n" + "="*60)
    print("        🏥 BMI (Body Mass Index) Calculator 🏥")
    print("="*60)
    print("\nPlease choose your preferred unit system:")
    print("\n📏 Unit System Options:")
    print("   1. Metric System")
    print("      • Weight in kilograms (kg) - Example: 70.5")
    print("      • Height in meters (m) - Example: 1.75")
    print("   2. Imperial System")
    print("      • Weight in pounds (lbs) - Example: 155.5")
    print("      • Height in inches (in) - Example: 69")
    print("-" * 60)
    
    while True:
        try:
            choice = input("\n👉 Enter your choice (1 or 2): ").strip()
            
            if choice == '1':
                unit_system = 'metric'
                print("\n📊 Metric System Selected")
                print("Please enter your measurements:")
                weight = float(input("⚖️  Weight (kg): "))
                
                if weight <= 0:
                    print("❌ Weight must be a positive number. Please try again.")
                    continue
                    
                height = float(input("📏 Height (meters): "))
                
                if height <= 0:
                    print("❌ Height must be a positive number. Please try again.")
                    continue
                    
                break
                
            elif choice == '2':
                unit_system = 'imperial'
                print("\n📊 Imperial System Selected")
                print("Please enter your measurements:")
                weight = float(input("⚖️  Weight (lbs): "))
                
                if weight <= 0:
                    print("❌ Weight must be a positive number. Please try again.")
                    continue
                    
                height = float(input("📏 Height (inches): "))
                
                if height <= 0:
                    print("❌ Height must be a positive number. Please try again.")
                    continue
                    
                break
                
            else:
                print("\n❌ Invalid choice. Please enter 1 for Metric or 2 for Imperial")
                
        except ValueError:
            print("\n❌ Please enter valid numbers only. No letters or special characters.")
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted by user. Goodbye!")
            exit()
    
    return weight, height, unit_system

def main():
    """
    Main function to run the BMI Calculator
    """
    try:
        weight, height, unit_system = get_user_input()
        
        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height, unit_system)
        
        # Get category and recommendation
        category = get_bmi_category(bmi)
        recommendation = get_health_recommendation(category)
        
        # Display results
        display_bmi_result(bmi, category, recommendation)
        
        # Show BMI categories reference
        print("\nBMI Categories Reference:")
        print("Underweight: < 18.5")
        print("Normal weight: 18.5 - 24.9")
        print("Overweight: 25 - 29.9")
        print("Obese: ≥ 30")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Unit tests
def test_bmi_calculator():
    """Test function for BMI calculator"""
    # Test metric system
    assert calculate_bmi(70, 1.75, 'metric') == 22.86
    assert calculate_bmi(60, 1.70, 'metric') == 20.76
    
    # Test imperial system
    assert calculate_bmi(154, 68, 'imperial') == 23.41
    
    # Test categories
    assert get_bmi_category(17.0) == "Underweight"
    assert get_bmi_category(22.0) == "Normal weight"
    assert get_bmi_category(27.0) == "Overweight"
    assert get_bmi_category(32.0) == "Obese"
    
    print("All tests passed!")

if __name__ == "__main__":
    main()
    
