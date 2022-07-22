Chart.defaults.font.size = 20;

const enrolleesLabels = schoolYears

  const enrolleesData = {
    labels: enrolleesLabels,
    datasets: [{
      label: 'All',
      backgroundColor: 'rgb(142, 68, 173)',
      borderColor: 'rgb(142, 68, 173)',
      data: allData,
    },
    {
        label: 'Male',
        backgroundColor: 'rgb(52, 152, 219)',
        borderColor: 'rgb(52, 152, 219)',
        data: maleData,
    },
    {
        label: 'Female',
        backgroundColor: 'rgb(231, 76, 60 )',
        borderColor: 'rgb(231, 76, 60 )',
        data: femaleData,
    },
]
  };

  const enrolleesConfig = {
    type: 'line',
    data: enrolleesData,
    options: {}
  };


  const enrollmentChart = new Chart(
    document.getElementById('enrollees-chart'),
    enrolleesConfig
  );


  new Chart(document.getElementById("average-grade-chart"), {
    type: 'bar',
    data: {
      labels: ["Lives in Malabon and Quezon City", "Lives Outside Malabon and Quezon City"],
      datasets: [
        {
          label: "Nursery",
          backgroundColor: "#E74C3C",
          data: nurseryData
        }, {
          label: "Kinder",
          backgroundColor: "#F1C40F",
          data: kinderData
        }
      ]
    },
    options: {
      title: {
        display: true,
      },
      scales: {
        y: {
          min: 75,
          max: 100,
          ticks: {
            stepSize: 5
          }
          
        }
      }
    }
});



const totalEnrolleesData = {
  labels: ['Malabon City', 'Quezon City'],
  datasets: [
    {
      label: 'Nursery (Male)',
      data: nurseryMale,
      backgroundColor: "#3498DB",
      stack: 'Stack 0',
    },
    {
      label: 'Nursery (Female)',
      data: nurseryFemale,
      backgroundColor: "#E74C3C",
      stack: 'Stack 0',
    },
    {
      label: 'Kinder (Male)',
      data: kinderMale,
      backgroundColor: "#1ABC9C",
      stack: 'Stack 1',
    },

    {
      label: 'Kinder (Female)',
      data: kinderFemale,
      backgroundColor: "#9B59B6",
      stack: 'Stack 1',
    },
  ]
};
// </block:setup>

// <block:config:0>
const totalEnrolleesConfig = {
  type: 'bar',
  data: totalEnrolleesData,
  options: {
    plugins: {
    },
    responsive: true,
    interaction: {
      intersect: false,
    },
    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true,
        ticks: {
          stepSize: 1
        }
      }
    }
  }
};


const totalEnrollees = new Chart(
  document.getElementById('total-enrollees-chart'),
  totalEnrolleesConfig
);






