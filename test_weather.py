from utils.weather import weather_report

report = weather_report("Mysuru")

print()

for k, v in report.items():
    print(k, ":", v)