const sidebar = document.getElementById('sidebar');
const mainContent = document.querySelector('.main-content');

// Toggle sidebar visibility
document.getElementById('hamburger').addEventListener('click', function() {
    sidebar.classList.toggle('hide');
    mainContent.classList.toggle('expanded');
});



// Toggle between Grid and List views
function setGridView() {
    const courseContainer = document.getElementById('courses');
    courseContainer.className = 'course-grid';
    resetPagination();
}

function setListView() {
    const courseContainer = document.getElementById('courses');
    courseContainer.className = 'course-list';
    resetPagination();
}

function filterCourses() {
    let input = document.getElementById('courseSearch').value.toLowerCase();  // Get the search input
    let courseItems = document.getElementsByClassName('course-item');  // Get all course-item elements

    for (let i = 0; i < courseItems.length; i++) {
        let courseTitle = courseItems[i].getElementsByTagName('h3')[0].innerText.toLowerCase();  // Get the course title

        // Show or hide the course-item based on the search input
        if (courseTitle.includes(input)) {
            courseItems[i].style.display = '';  // Show course-item
        } else {
            courseItems[i].style.display = 'none';  // Hide course-item
        }
    }
}


// Pagination Variables
let currentPage = 1;
const coursesPerPage = 6; // Increased to 8 courses per page

// Initialize Pagination on Page Load
document.addEventListener('DOMContentLoaded', function () {
    setupPagination();
});

// Setup Pagination
function setupPagination() {
    const courses = document.getElementsByClassName('course-item');
    const totalCourses = courses.length;
    const totalPages = Math.ceil(totalCourses / coursesPerPage);

    if (currentPage > totalPages) currentPage = totalPages;

    showPage(currentPage);

    document.getElementById('page-info').innerText = `Page ${currentPage} of ${totalPages}`;
}

// Show Specific Page
function showPage(page) {
    const courses = document.getElementsByClassName('course-item');
    const totalCourses = courses.length;
    const totalPages = Math.ceil(totalCourses / coursesPerPage);

    if (page < 1) page = 1;
    if (page > totalPages) page = totalPages;

    for (let i = 0; i < totalCourses; i++) {
        courses[i].style.display = 'none';
    }

    let start = (page - 1) * coursesPerPage;
    let end = start + coursesPerPage;
    if (end > totalCourses) end = totalCourses;

    for (let i = start; i < end; i++) {
        courses[i].style.display = '';
    }

    document.getElementById('page-info').innerText = `Page ${page} of ${totalPages}`;

    currentPage = page;
}

// Change Page
function changePage(direction) {
    const courses = document.getElementsByClassName('course-item');
    const totalCourses = courses.length;
    const totalPages = Math.ceil(totalCourses / coursesPerPage);

    let newPage = currentPage + direction;

    if (newPage < 1) newPage = 1;
    if (newPage > totalPages) newPage = totalPages;

    showPage(newPage);
}

// Reset Pagination when view changes
function resetPagination() {
    currentPage = 1;
    setupPagination();
}


let slideIndex = 0;
showSlides(); // Initial call to show slides

// Function to show the slides
function showSlides() {
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");

  // Hide all slides
  for (let i = 0; i < slides.length; i++) {
    slides[i].classList.remove('active');
  }

  // Remove active class from dots
  for (let i = 0; i < dots.length; i++) {
    dots[i].classList.remove('active-dot');
  }

  // Increment slideIndex
  slideIndex++;

  // Reset the slideIndex if it's greater than the number of slides
  if (slideIndex > slides.length) { 
    slideIndex = 1;
  }

  // Display the active slide and active dot
  slides[slideIndex - 1].classList.add('active');
  dots[slideIndex - 1].classList.add('active-dot');

  // Change slides every 5 seconds (5000 milliseconds)
  setTimeout(showSlides, 5000); 
}

// Function to show the current slide when a dot is clicked
function currentSlide(n) {
  slideIndex = n;
  showSlides();
}



