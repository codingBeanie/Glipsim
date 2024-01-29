document.addEventListener('DOMContentLoaded', function() {
    fetch_data();
});

function fetch_data() { 
    fetch('api/get_households')
        .then(response => response.json())
        .then(data => {
            const parentDiv = document.getElementById('data');
            parentDiv.className = 'd-flex flex-wrap m-2';

            data.forEach(household => {
                const cardDiv = document.createElement('div');
                cardDiv.className = 'card w-25 m-2';

                const cardBody = document.createElement('div');
                cardBody.className = 'card-body';
                cardDiv.appendChild(cardBody);

                const cardTitle = document.createElement('h5');
                cardTitle.className = 'card-title';
                cardTitle.innerHTML = household.name;
                cardBody.appendChild(cardTitle);

                const cardSubtitle = document.createElement('h6');
                cardSubtitle.className = 'card-subtitle mb-2 text-muted';
                cardSubtitle.innerHTML = "Resources: " + household.resources + " Members: " + household.count_members_alive;
                cardBody.appendChild(cardSubtitle);

                household.members.forEach(member => {
                    const cardText = document.createElement('p');
                    cardText.className = 'card-text';
                    cardText.innerHTML = member.full_name + " (" + member.age + ") [] - Health: " + member.health;
                    cardBody.appendChild(cardText);
                });

                parentDiv.appendChild(cardDiv);
            });
        })
        .catch(error => console.error(error));
}