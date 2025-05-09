# MCP Farming Demo  
[![License](https://img.shields.io/badge/license-MIT-blue.svg )](https://opensource.org/licenses/MIT )  
*A project to demonstrate MCP capabilities with Real-Time Database Querying & Data Analysis using agricultural data*  

---

## 📌 Overview  
This repository showcases how to integrate AI with real-world data using **MCP (Model Context Protocol)**. It includes:  
- A SQLite database schema for farming data (crops, fields, harvests).  
- Synthetic data generation scripts for crop yield analysis.  
- Future MCP server integration for AI-driven queries (e.g., *"Which crop has the highest yield?"*).  

---

## 📁 Project Structure  
```
mcp-farming-demo/  
│  
├── data/               # Stores SQLite DB and synthetic data  
├── scripts/            # Python scripts for data generation  
├── docs/               # Documentation (e.g., MCP setup guides)  
├── README.md           # Project overview  
└── .gitignore          # Excludes large files (e.g., SQLite DB backups)  
```  

---

## 🛠️ Setup Instructions  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/MCP-Learning/mcp-query-db.git   
   cd mcp-query-db  
   ```  

2. **Create the database and tables**:  
   ```bash  
   python3 scripts/generate_db.py  
   ```  

3. **Generate synthetic data**:  
   ```bash  
   python3 scripts/generate_data.py  
   ```  

4. **Query the database**:  
   Use [DB Browser for SQLite](https://sqlitebrowser.org/ ) to explore `data/farming.db`.  

---

## 📊 Example SQL Queries  
Run these in DB Browser for SQLite to analyze data:  

### **Yield per Hectare by Crop**  
```sql  
SELECT c.name AS crop,  
       ROUND(h.yield_tons / f.area_hectares, 2) AS yield_per_hectare  
FROM harvests h  
JOIN crops c ON h.crop_id = c.crop_id  
JOIN fields f ON h.field_id = f.field_id;  
```  

### **Total Yield by Crop**  
```sql  
SELECT c.name, SUM(h.yield_tons) AS total_yield  
FROM harvests h  
JOIN crops c ON h.crop_id = c.crop_id  
GROUP BY c.name;  
```  

---

## 📜 License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  

---

## 🤝 Acknowledgments  
- Inspired by [MCP's universal connectivity vision](https://modelcontextprotocol.com/ )  