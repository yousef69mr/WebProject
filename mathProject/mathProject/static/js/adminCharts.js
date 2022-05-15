var hours = [];
var text_hour;
var hour;
for (var i = 0; i < 24; i++) {
    hour = i;
    if(hour>12){
        hour = i - 12;
    }
   if (hour > 9) {
      text_hour = hour+':00';
   } else {
      text_hour = '0'+hour+':00';
   }
   if (i<12){
      text_hour += ' AM';
   }else{
       text_hour+= ' PM';
   }
   hours.push(text_hour);
}

console.log(hours)

const ctx = document.getElementById('myChart_1').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Female' ,'Male'],
        datasets: [{
            label: ['Female' ,'Male'],
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
              display: true,
              text: 'Gender Dounghnut Chart'
            },
        },
    }
});


/*******************************************************************/

const ctx2 = document.getElementById('myChart_2').getContext('2d');
const myChart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['Physics' ,'Biology','Mathmatics' , 'Arabic', 'Statistics', 'French'],
        datasets: [{
            label: 'Number of Students',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            title: {
              display: true,
              text: 'Number of Students in each Subject'
            },
        },
    }
});


/*******************************************************************/

const ctx3 = document.getElementById('myChart_3').getContext('2d');
const myChart3 = new Chart(ctx3, {
    type: 'polarArea',
    data: {
        labels: ['Physics' ,'Biology','Mathmatics' , 'Arabic', 'Statistics', 'French'],
        datasets: [{
            label: 'Number of Files',
            data: [12, 21, 45, 28, 10, 33],
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
                'rgba(255, 159, 64, 0.6)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: {
              display: true,
              text: 'Number of Files in each Subject'
            },
        },
    }
});


/*******************************************************************/

const ctx4 = document.getElementById('myChart_4').getContext('2d');
const myChart4 = new Chart(ctx4, {
    
    data: {
        labels: hours,
        datasets: [{
            type: 'line',
            label: '1st Sec',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            fill:false,
            tension:0.1,
            
        },{
            type: 'line',
            label: '3rd Prep',
            data: [22, 2, 0, 5, 21, 9],
            backgroundColor: 'rgba(255, 99, 132, 0.6)',
                
            
            borderColor: 'rgba(255, 99, 132, 1)',
            fill:false,
            tension:0.1,
            
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                display: true,
                title: {
                    display: true,
                    text: 'Logins'
                }
            },
            x:{
                display: true,
                title: {
                    display: true,
                    text: 'Hours'
                }
            }
        },
        plugins: {
            title: {
              display: true,
              text: 'Daily Login Activity of Users'
            },
        },
        
    }
});
