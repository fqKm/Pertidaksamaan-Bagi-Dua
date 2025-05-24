const form = document.querySelector('form');
const hasilDiv = document.getElementById('hasil');
const hasilValue = document.getElementById('hasil-value');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const submitBtn = document.querySelector('.submit-btn');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Menghitung...';
    submitBtn.style.opacity = '0.7';
    
    setTimeout(() => {
        hasilValue.textContent = 'Hasil perhitungan akan ditampilkan di sini';
        hasilDiv.style.display = 'block';
        
        submitBtn.textContent = originalText;
        submitBtn.style.opacity = '1';
    }, 1500);
});

const inputs = document.querySelectorAll('input, select');
inputs.forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'translateY(-2px)';
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.style.transform = 'translateY(0)';
    });
});
