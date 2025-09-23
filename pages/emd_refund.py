"""
EMD Refund Tool Page
"""

import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="EMD Refund | PWD Tools",
    page_icon="💰",
    layout="wide"
)

def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name.strip())
    return safe[:80] or "receipt"

def build_full_page_receipt_html(contractor_name: str, emd_amount: float, refund_amount: float, 
                                tender_number: str, work_description: str, deduction_reason: str, 
                                deduction_amount: float, refund_percentage: float) -> str:
    """Generate full page hand receipt similar to Excel se EMD tool"""
    
    # Format amounts
    emd_amount_str = f"{emd_amount:,.2f}"
    refund_amount_str = f"{refund_amount:,.2f}"
    deduction_amount_str = f"{deduction_amount:,.2f}"
    
    # Escape single quotes for JavaScript
    contractor_js = contractor_name.replace("'", r"\'")
    work_js = work_description.replace("'", r"\'")
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>EMD Refund Hand Receipt</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 0; }}
    .container {{ width: 100%; max-width: 900px; margin: 20px auto; border: 1px solid #e1e8e3; padding: 24px; box-sizing: border-box; background: #fff; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.08); }}
    .header {{ text-align: center; margin-bottom: 10px; color: #2E8B57; }}
    .details {{ margin-bottom: 1px; }}
    .amount-words {{ font-style: italic; }}
    .signature-area, .offices {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
    .signature-area td, .signature-area th, .offices td, .offices th {{ border: 1px solid #ccc; padding: 5px; text-align: left; }}
    .offices td, .offices th {{ border-color: #000; word-wrap: break-word; }}
    .input-field {{ border-bottom: 1px dotted #ccc; padding: 3px; width: calc(100% - 10px); display: inline-block; }}
    .bottom-left-box {{ position: relative; border: 2px solid black; padding: 10px; width: 300px; text-align: left; margin-top: 12px; }}
    .bottom-left-box p {{ margin: 3px 0; }}
    .blue-text {{ color: blue; }}
    @media print {{
      @page {{ size: A4 portrait; margin: 0; }}
      body {{ margin: 0; padding: 0; }}
      .container {{ border: none; width: 210mm; min-height: 297mm; margin: 0; padding: 20mm; box-sizing: border-box; }}
      .input-field {{ border: none; }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div id="receipt-content">
      <div class="header">
        <h2>Payable to: - {contractor_js} (Contractor)</h2>
        <h2>HAND RECEIPT (RPWA 28)</h2>
        <p>(Referred to in PWF&A Rules 418,424,436 & 438)</p>
        <p>Division - PWD Electric Division, Udaipur</p>
      </div>
      <div class="details">
        <p><strong>(1)</strong> Cash Book Voucher No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <p><strong>(2)</strong> Cheque No. and Date &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
        <p><strong>(3)</strong> Pay for ECS Rs. {refund_amount_str}/- (Rupees <span id="amount-words" class="amount-words"></span>)</p>
        <p><strong>(4)</strong> Paid by me</p>
        <p><strong>(5)</strong> Received from The Executive Engineer PWD Electric Division, Udaipur the sum of Rs. {refund_amount_str}/- (Rupees <span id="amount-words-2" class="amount-words"></span>)</p>
        <p><strong>Name of work for which payment is made:</strong> <span id="work-name" class="input-field">{work_js}</span></p>
        <p><strong>Chargeable to Head:</strong>- 8443 [EMD-Refund]</p>
        <table class="signature-area">
          <tr><td>Witness</td><td>Stamp</td><td>Signature of payee</td></tr>
          <tr><td>Cash Book No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Page No. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td></td></tr>
        </table>
        <table class="offices">
          <tr><td>For use in the Divisional Office</td><td>For use in the Accountant General's office</td></tr>
          <tr><td>Checked</td><td>Audited/Reviewed</td></tr>
          <tr><td>Accounts Clerk</td><td>DA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Auditor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supdt. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G.O.</td></tr>
        </table>
      </div>
      <div class="bottom-left-box">
        <p class="blue-text">Passed for Rs. {refund_amount_str}</p>
        <p class="blue-text" id="amount-words-3">In Words Rupees: </p>
        <p class="blue-text">Chargeable to Head:- 8443 [EMD-Refund]</p>
        <div class="seal">
          <p>Ar.</p>
          <p>D.A.</p>
          <p>E.E.</p>
        </div>
      </div>
    </div>
  </div>
  <script>
    function convertNumberToWords(num) {{
      const ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
      const tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
      const teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
      const crore = " Crore ";
      const lakh = " Lakh ";
      const thousand = " Thousand ";
      const hundred = " Hundred ";
      const andWord = " and ";
      
      if (!num || isNaN(num)) return "Zero";
      
      // Remove any commas and convert to number
      num = parseFloat(num.toString().replace(/,/g, ''));
      if (isNaN(num)) return "Zero";
      
      // Round to 2 decimal places and get the integer part
      const rupees = Math.floor(num);
      const paise = Math.round((num - rupees) * 100);
      
      let words = "";
      
      // Process rupees part
      if (rupees > 0) {{
        let r = rupees;
        if (Math.floor(r / 10000000)) {{ words += convertNumberToWords(Math.floor(r / 10000000)) + crore; r %= 10000000; }}
        if (Math.floor(r / 100000)) {{ words += convertNumberToWords(Math.floor(r / 100000)) + lakh; r %= 100000; }}
        if (Math.floor(r / 1000)) {{ words += convertNumberToWords(Math.floor(r / 1000)) + thousand; r %= 1000; }}
        if (Math.floor(r / 100)) {{ words += convertNumberToWords(Math.floor(r / 100)) + hundred; r %= 100; }}
        if (r > 0) {{
          if (words !== "") words += andWord;
          if (r < 10) words += ones[r];
          else if (r < 20) words += teens[r - 10];
          else {{ 
            words += tens[Math.floor(r / 10)]; 
            if (r % 10 > 0) words += " " + ones[r % 10]; 
          }}
        }}
        words += " Rupees";
      }}
      
      // Process paise part
      if (paise > 0) {{
        if (words !== "") words += " and ";
        if (paise < 10) words += ones[paise];
        else if (paise < 20) words += teens[paise - 10];
        else {{ 
          words += tens[Math.floor(paise / 10)]; 
          if (paise % 10 > 0) words += " " + ones[paise % 10]; 
        }}
        words += " Paise";
      }}
      
      return words || "Zero Rupees";
    }}
    
    // Format the amount with commas
    function formatAmount(amount) {{
      return amount.toString().replace(/\B(?=(\d{{3}})+(?!\d))/g, ",");
    }}
    
    // Update all amount in words placeholders
    document.addEventListener('DOMContentLoaded', function() {{
      const amount = {refund_amount};
      const amountInWords = convertNumberToWords(amount);
      document.querySelectorAll('.amount-words').forEach(el => {{
        el.textContent = amountInWords + ' only';
      }});
      document.getElementById('amount-words-3').textContent = 'In Words Rupees: ' + amountInWords + ' Only';
    }});
  </script>
</body>
</html>
""".format(
        contractor_name=contractor_js,
        emd_amount=emd_amount,
        refund_amount=refund_amount,
        refund_amount_str=refund_amount_str,
        work_description=work_js,
        deduction_reason=deduction_reason.replace("'", r"\'") if deduction_reason else "",
        deduction_amount=deduction_amount,
        deduction_amount_str=deduction_amount_str,
        refund_percentage=refund_percentage,
        tender_number=tender_number.replace("'", r"\'")
    )
    
    return html

# Custom CSS
st.markdown("""
<style>
    .tool-header {
        background: linear-gradient(135deg, #F59E0B 0%, #EF4444 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .calculator-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .result-card {
        background: linear-gradient(135deg, #10B981 0%, #8B5CF6 100%);
        color: white;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="tool-header">
    <h1>💰 EMD Refund Calculator</h1>
    <h3>Generate EMD refund receipts and documentation</h3>
</div>
""", unsafe_allow_html=True)

# Tool description
st.markdown("""
<div style="background: #FEF3C7; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <p>Calculate Earnest Money Deposit (EMD) refunds for contractors. Enter the tender details and contractor information 
    to generate refund calculations and documentation.</p>
</div>
""", unsafe_allow_html=True)

# EMD Refund Calculator
st.markdown("### 🧮 EMD Refund Calculator")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="calculator-card">', unsafe_allow_html=True)
    st.markdown("#### Tender Details")
    tender_number = st.text_input("Tender Number", "PWD/TEND/2025/001")
    work_description = st.text_area("Work Description", "Road Construction Project", height=100)
    contractor_name = st.text_input("Contractor Name", "ABC Construction Company")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="calculator-card">', unsafe_allow_html=True)
    st.markdown("#### Financial Details")
    emd_amount = st.number_input("Original EMD Amount (₹)", value=50000.0, step=1000.0, format="%.2f")
    refund_percentage = st.slider("Refund Percentage", 0, 100, 100)
    deduction_reason = st.text_area("Deduction Reason (if any)", "", height=100)
    deduction_amount = st.number_input("Deduction Amount (₹)", value=0.0, step=100.0, format="%.2f")
    st.markdown("</div>", unsafe_allow_html=True)

# Calculate button
if st.button("🧮 Calculate Refund", type="primary", use_container_width=True):
    # Calculate refund
    refund_amount = emd_amount * (refund_percentage / 100) - deduction_amount
    
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Refund Calculation Result")
    st.markdown(f"<h2>₹{refund_amount:,.2f}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p>Refund Amount for {contractor_name}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Detailed breakdown
    st.markdown("### 📋 Detailed Breakdown")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Original EMD", f"₹{emd_amount:,.2f}")
    
    with col2:
        st.metric("Deductions", f"₹{deduction_amount:,.2f}")
    
    with col3:
        st.metric("Net Refund", f"₹{refund_amount:,.2f}")
    
    # Generate receipts
    st.markdown("### 📄 Refund Receipt Preview")
    
    # Simple receipt preview
    receipt_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>EMD Refund Receipt - {contractor_name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .receipt {{ border: 2px solid #F59E0B; border-radius: 10px; padding: 20px; max-width: 800px; margin: 0 auto; }}
            .header {{ text-align: center; color: #F59E0B; }}
            .details {{ margin: 20px 0; }}
            .signature {{ margin-top: 30px; display: flex; justify-content: space-between; }}
            .signature div {{ width: 30%; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="receipt">
            <div class="header">
                <h2>EMD REFUND RECEIPT</h2>
                <p>Public Works Department, Udaipur</p>
            </div>
            <div class="details">
                <p><strong>Tender Number:</strong> {tender_number}</p>
                <p><strong>Work Description:</strong> {work_description}</p>
                <p><strong>Contractor:</strong> {contractor_name}</p>
                <p><strong>Original EMD Amount:</strong> ₹{emd_amount:,.2f}</p>
                <p><strong>Refund Percentage:</strong> {refund_percentage}%</p>
                <p><strong>Deduction Reason:</strong> {deduction_reason if deduction_reason else "None"}</p>
                <p><strong>Deduction Amount:</strong> ₹{deduction_amount:,.2f}</p>
                <p><strong>Net Refund Amount:</strong> ₹{refund_amount:,.2f}</p>
                <p><strong>Date:</strong> {st.session_state.get('date', 'N/A')}</p>
            </div>
            <div class="signature">
                <div>
                    <p>Prepared By</p>
                    <p>_________________</p>
                </div>
                <div>
                    <p>Checked By</p>
                    <p>_________________</p>
                </div>
                <div>
                    <p>Authorized Signatory</p>
                    <p>_________________</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    st.components.v1.html(receipt_html, height=500, scrolling=True)
    
    # Generate full page receipt
    full_page_receipt_html = build_full_page_receipt_html(
        contractor_name=contractor_name,
        emd_amount=emd_amount,
        refund_amount=refund_amount,
        tender_number=tender_number,
        work_description=work_description,
        deduction_reason=deduction_reason,
        deduction_amount=deduction_amount,
        refund_percentage=refund_percentage
    )
    
    # Download options
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Download Simple Receipt",
            data=receipt_html,
            file_name=f"emd_refund_simple_{sanitize_filename(contractor_name)}.html",
            mime="text/html",
            use_container_width=True
        )
    
    with col2:
        st.download_button(
            label="📄 Download Full Page Receipt",
            data=full_page_receipt_html,
            file_name=f"emd_refund_full_{sanitize_filename(contractor_name)}.html",
            mime="text/html",
            use_container_width=True
        )

# Back to main page
if st.button("🏠 Back to Main Page", use_container_width=True):
    st.switch_page("web_main.py")