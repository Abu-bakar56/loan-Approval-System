function validateForm() {
    const formElements = document.querySelectorAll('#loanForm input, #loanForm select');
    for (let element of formElements) {
        if (!element.value) {
            alert('Please fill in all required fields.');
            return false;
        }
    }
    return true;
}

function submitForm() {
    if (validateForm()) {
        const form = document.getElementById('loanForm');
        const formData = new FormData(form);

        fetch('/submit', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            const predictionResult = document.getElementById('predictionResult');
            const resultImage = document.createElement('img'); 

            predictionResult.innerText = `${data.name}, your application for a loan is ${data.prediction === "Approved" ? "approved" : "rejected"}.`;


           
            if (data.prediction === 'Approved') {
                resultImage.src = '/static/2.jpg';  
                resultImage.alt = 'Loan Approved';
                resultImage.style.marginLeft="20px";
            } else if (data.prediction === 'Rejected') {
                resultImage.src = '/static/3.png'; 
                resultImage.alt = 'Loan Rejected';
                resultImage.style.marginLeft="60px";
            }

            resultImage.style.display = 'block';  

            

            
            const imageContainer = document.getElementById('imageContainer');
            imageContainer.innerHTML = ''; 
            imageContainer.appendChild(resultImage);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while submitting the form. Please try again.');
        });
    }
}


