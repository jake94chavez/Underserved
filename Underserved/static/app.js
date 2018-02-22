// add event listener to all buttons
// if the button has no class 'clicked', add it
// if it does have class 'clicked', remove it


const clickHandler = () => {
	let clicked = document.getElementsByTagName('button').getAttribute('aria-pressed')
	if ( clicked = True ) {
		// append 
	}
}

let tagsList = []

const clickAppend = (e) => {
	let tagIsOn = true
	if (tagIsOn) {
		tagsList.push(e.innerText)
	}
	console.log(tagsList)
}