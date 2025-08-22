import os

def create_folders():
    print("🏗️  Creating portfolio folders...")
    folders = [
        "data/original-data",
        "data/processed-data", 
        "powerbi/screenshots",
        "powerbi/reports",
        "excel-analysis",
        "insights"
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"   ✅ Created: {folder}")

def create_readme():
    print("📄 Creating README.md...")
    readme = """# 📊 Superstore Business Analysis Portfolio

**Comprehensive sales performance and profitability analysis using Excel and Power BI**

## 🎯 Project Objective
Analyze Superstore commercial performance to identify sales trends, growth opportunities, and profitability improvement areas.

## 📊 Key Results
- **Total Revenue**: €2,297.2K
- **Total Profit**: €286.4K  
- **Profit Margin**: 12.5%
- **Sales Growth**: +51% from 2014 to 2017

## 🏆 Top Insights
- **Technology** leads sales (€836K revenue, 17.4% margin)
- **Strong Q4 seasonality** (Nov-Dec surge)
- **Furniture needs attention** (2.5% margin - improvement needed)

## 🛠️ Tools Used
- **Microsoft Excel**: Pivot tables, advanced formulas, data cleaning
- **Power BI Service**: Interactive dashboards, visualizations, KPIs

---
**Contact**: [Your LinkedIn/Email]
"""
    
    with open("README.md", "w") as f:
        f.write(readme)
    print("   ✅ Created: README.md")

if __name__ == "__main__":
    print("🚀 Creating Superstore Portfolio...")
    create_folders()
    create_readme()
    print("\n✅ Basic structure complete!")
    print("📁 Next: Add your Excel file and Power BI screenshots")
