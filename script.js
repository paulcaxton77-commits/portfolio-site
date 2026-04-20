// --- 1. DARK MODE LOGIC ---
const themeBtn = document.getElementById('theme-toggle');
themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    themeBtn.innerText = document.body.classList.contains('dark-mode') ? "Light Mode" : "Dark Mode";
});

// --- 2. KPLC CALCULATION LOGIC ---
function calculateTokens() {
    const budget = parseFloat(document.getElementById('budget').value);
    const dailyUsage = parseFloat(document.getElementById('appliance').value);
    const resultDiv = document.getElementById('result');

    if (isNaN(budget) || budget <= 0) {
        resultDiv.innerHTML = "Please enter a valid amount.";
        resultDiv.style.color = "red";
        return;
    }

    // Average cost per KPLC unit (approx 30 KES)
    const pricePerUnit = 30;
    const totalUnits = budget / pricePerUnit;
    const daysLasting = totalUnits / dailyUsage;

    resultDiv.style.color = "#27ae60";
    resultDiv.innerHTML = `
        <p>Units: ${totalUnits.toFixed(2)} kWh</p>
        <p>Est. Duration: ${daysLasting.toFixed(1)} Days</p>
    `;
}




function calculateBundle() {
    const size = parseFloat(document.getElementById('bundle-size').value);
    const unit = parseFloat(document.getElementById('size-unit').value);
    const price = parseFloat(document.getElementById('bundle-price').value);
    const resultDiv = document.getElementById('bundle-result');

    if (size > 0 && price > 0) {
        // Convert everything to MB for a fair fight
        const totalMB = size * unit;
        
        // Calculate how many MB you get for 1 Shilling
        const mbPerKes = totalMB / price;

        resultDiv.style.color = "#8e44ad";
        resultDiv.innerHTML = `
            <p>You get <strong>${mbPerKes.toFixed(2)} MB</strong> per Shilling.</p>
            <p>Total Data: ${totalMB.toFixed(0)} MB</p>
        `;
    } else {
        resultDiv.innerHTML = "Enter size and price!";
    }
}