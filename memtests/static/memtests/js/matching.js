let clickedCard = null;
let preventClick = false;
let score = 0;
document.getElementById("score").innerHTML = score;


const colors = [
	'red',
	'orange',
	'yellow',
	'green',
	'cyan',
	'blue',
	'purple',
	'pink'
]

//randomize color pairs 
const cards = [...document.querySelectorAll('.card-nb')];
for(let color of colors){
	const cardAIndex = parseInt(Math.random() * cards.length);
	const cardA = cards[cardAIndex];
	cards.splice(cardAIndex, 1);
	cardA.className += ` ${color}`;
	cardA.setAttribute('data-color', color);

	const cardBIndex = parseInt(Math.random() * cards.length);
	const cardB = cards[cardBIndex];
	cards.splice(cardBIndex, 1);
	cardB.className += ` ${color}`;
	cardB.setAttribute('data-color', color);
}

function onCardClicked(e) {
	const target = e.currentTarget;

	//no double clicking
	if(preventClick || target === clickedCard || target.className.includes('done')){
		return;
	}

	target.className = target.className
		.replace('color-hidden', '')
		.trim();
	target.className += ' done'; 

	if(!clickedCard){
		//if we haven't clicked a card, keep track of the card and display its color
		clickedCard = target;
	}
	else if(clickedCard){
		//if we have already clicked a card, check if the new card matches the old card color
		if(clickedCard.getAttribute('data-color') === target.getAttribute('data-color')){
			score++;
			document.getElementById("score").innerHTML = score;
			clickedCard = null;
		}
		else{
			preventClick = true;
			setTimeout(() => {
				clickedCard.className = clickedCard.className.replace('done', '').trim() + ' color-hidden';
				target.className = target.className.replace('done', '').trim() + 'color-hidden';
				clickedCard = null;
				preventClick = false;
			}, 500);
		}
	}

	
}


