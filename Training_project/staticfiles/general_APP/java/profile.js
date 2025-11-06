const sidebar = document.getElementById('sidebar');
const mainContent = document.querySelector('.profile-info');

// Toggle sidebar visibility
document.getElementById('hamburger').addEventListener('click', function() {
    sidebar.classList.toggle('hide');
    mainContent.classList.toggle('expanded');
});

// Get the tabs and sections by their IDs
const aboutTab = document.getElementById('aboutTab');
const coursesTab = document.getElementById('coursesTab');
const editProfileTab = document.getElementById('editProfileTab');

const aboutMeSection = document.getElementById('aboutMeSection');
const coursesSection = document.getElementById('coursesSection');
const editProfileSection = document.getElementById('editProfileSection');

// Function to handle the tab switch
function showSection(section) {
  // Hide all sections
  aboutMeSection.style.display = 'none';
  if (coursesSection) {
    coursesSection.style.display = 'none';
  }
  if (editProfileSection) {
    editProfileSection.style.display = 'none';
  }
  
  // Show the selected section
  section.style.display = 'block';
  
  // Remove active class from all tabs
  aboutTab.classList.remove('active');
  coursesTab.classList.remove('active');
  editProfileTab.classList.remove('active');
}

// Event listeners for tabs
aboutTab.addEventListener('click', function() {
  showSection(aboutMeSection);
  aboutTab.classList.add('active');
});

if (coursesTab && coursesSection) {
  coursesTab.addEventListener('click', function() {
    showSection(coursesSection);
    coursesTab.classList.add('active');
  });
}

if (editProfileTab && editProfileSection) {
  editProfileTab.addEventListener('click', function() {
    showSection(editProfileSection);
    editProfileTab.classList.add('active');
  });
}

// Handle profile form submission
const editProfileForm = document.getElementById('editProfileForm');
if (editProfileForm) {
  editProfileForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission for now

    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;

    // Update the profile card with new values
    document.querySelector('.profile-card h3').textContent = `${firstName} ${lastName}`;
    alert('Profile updated successfully!');
  });
}
