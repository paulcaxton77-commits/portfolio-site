function calculateAdvancedKPLC() {
    const amount = parseFloat(document.getElementById('kes-amount').value);
    const resultDiv = document.getElementById('kplc-result');

    if (isNaN(amount) || amount <= 0) {
        resultDiv.innerHTML = "Please enter a valid amount.";
        return;
    }

    // 2026 Estimated Effective Rates (Base + Levies + Taxes)
    // Lifeline: 0-30 units | Ordinary: 31-100 units | High: >100 units
    const LIFELINE_RATE = 28.45; 
    const ORDINARY_RATE = 34.20;

    let units = 0;
    let category = "";
    let tip = "";

    if (amount <= 900) {
        units = amount / LIFELINE_RATE;
        category = "Domestic Lifeline";
        tip = "You're in the cheapest tier. Keep it up!";
    } else {
        units = amount / ORDINARY_RATE;
        category = "Domestic Ordinary";
        tip = "⚠️ Higher usage detected. Check your water heater to save.";
    }

    resultDiv.innerHTML = `
        <h1 style="margin: 0; color: #4ade80;">${units.toFixed(2)}</h1>
        <p style="margin: 5px 0;">Units Estimated</p>
        <span style="font-size: 0.8em; background: #333; padding: 4px 8px; border-radius: 5px;">${category}</span>
        <p style="font-size: 0.85em; color: #eab308; margin-top: 15px;">${tip}</p>
    `;
}