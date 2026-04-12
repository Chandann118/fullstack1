from django.shortcuts import render

def index(request):
    result_c = None
    result_f = None
    result_k = None
    input_val = ""
    from_unit = "C"

    if request.method == "POST":
        try:
            input_val = request.POST.get("temperature", "")
            from_unit = request.POST.get("unit", "C")
            
            if input_val:
                val = float(input_val)
                
                # Convert to Celsius first
                if from_unit == "C":
                    temp_c = val
                elif from_unit == "F":
                    temp_c = (val - 32) * 5/9
                elif from_unit == "K":
                    temp_c = val - 273.15
                
                # Convert from Celsius to others
                result_c = round(temp_c, 2)
                result_f = round((temp_c * 9/5) + 32, 2)
                result_k = round(temp_c + 273.15, 2)
        except ValueError:
            pass

    context = {
        "result_c": result_c,
        "result_f": result_f,
        "result_k": result_k,
        "input_val": input_val,
        "from_unit": from_unit,
    }
    return render(request, "converter/index.html", context)
