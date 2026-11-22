# DukaanMitra MCP Connector

> **Official Model Context Protocol (MCP) Gateway for DukaanMitra — Connect Kirana Stores, Billing, Udhaar & Inventory directly to Google Gemini, Claude & Autonomous AI Agents.**

---

## Why DukaanMitra MCP?

DukaanMitra MCP bridges sovereign Indian retail operations with next-generation LLMs (Google Gemini 1.5/2.0, Claude 3.5, OpenAI). It allows AI models to natively read live store inventory, record vernacular voice transactions, compute GST breakdowns, and verify compliance with deterministic zero-trust safeguards.

---

## Included MCP Tools

| Tool | Parameters | Description |
|---|---|---|
| `get_inventory_summary` | `tenant_id`, `low_stock_only` | Retrieves real-time stock levels, valuations, and low-inventory alerts. |
| `record_voice_transaction` | `tenant_id`, `transcript`, `amount` | Parses Kirana voice notes ("Ramesh ko 2 packet aata udhaar") into structured transactions. |
| `detect_stockout_risk` | `tenant_id`, `lead_days` | AI forecasting of inventory depletion based on sales velocity. |
| `create_purchase_order_draft` | `tenant_id`, `supplier_name`, `items` | Generates supplier PO draft with dynamic wholesale price comparison. |
| `validate_gst_invoice` | `gstin`, `amount`, `rate` | Deterministic Indian GST calculator (CGST, SGST, IGST breakdown). |
| `reconcile_gstr2b` | `tenant_id`, `period` | Matches purchase ledger against GSTR-2B compliance records. |
| `get_magic_insights` | `tenant_id` | Business intelligence summary: top selling items, dead stock, cashflow health. |

---

## Quick Setup with Google Gemini

### 1. Install & Run Server
```bash
git clone https://github.com/dukaanmitra-ai/dukaanmitra-mcp.git
cd dukaanmitra-mcp
pip install -r requirements.txt
python main.py
```
Server runs at `http://localhost:8001/mcp`.

### 2. Gemini GenAI SDK Integration (TypeScript)
```typescript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
// Connect DukaanMitra MCP tool schemas to Gemini function calling
const model = ai.models.get("gemini-1.5-flash");
```

---

## License
MIT (c) 2026 Amit Sharma & DukaanMitra AI.
