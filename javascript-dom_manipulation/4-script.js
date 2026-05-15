// Select the element with the ID add_item
const addItemTrigger = document.querySelector('#add_item');

// Add a click event listener to the trigger
addItemTrigger.addEventListener('click', function () {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  
  // Select the ul element with the class my_list
  const list = document.querySelector('.my_list');
  
  // Append the new li element to the list
  list.appendChild(newItem);
});
