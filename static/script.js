document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.sidebar ul li a');
    const contentDivs = document.querySelectorAll('.content div');

    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('data-target');
            contentDivs.forEach(div => {
                if (div.id === targetId) {
                    div.classList.add('active');
                } else {
                    div.classList.remove('active');
                }
            });
        });
    });

    const pwmForm = document.getElementById('pwmForm');

    pwmForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const dutyCycle = document.getElementById('dutyCycle').value;

        const data = {
            dutyCycle: parseFloat(dutyCycle)
        };

        fetch('/api/rpi/pwm1', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                alert('Настройки PWM успешно сохранены!');
            } else {
                alert('Ошибка при сохранении настроек PWM.');
            }
        })
        .catch(error => {
            console.error('Произошла ошибка:', error);
            alert('Произошла ошибка при отправке данных.');
        });
    });
});