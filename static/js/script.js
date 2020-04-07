/*
    Quora Clone
*/


// model related code
const model = $('.model_container');
const modelans = $('.model_container_answer');
const backdrop = $('.backdrop');
const body = $('body');
const avatar = $('#avatar');

function openModelans(e) {
    modelans.fadeIn(200);
    backdrop.show();
    body.css('overflow','hidden');
}

function closeModelans(e) {
    modelans.hide();
    backdrop.fadeOut(500);
    body.css('overflow','scroll');
}

function openModel(e) {
    model.fadeIn(200);
    backdrop.show();
    
    body.css('overflow','hidden');
}

function closeModel(e) {
    model.hide();
    backdrop.fadeOut(500);
    body.css('overflow','scroll');
}


function removeActiveTab(){
    $('#Home').removeClass('active');
    $('#Question').removeClass('active');
    $('#Answer').removeClass('active');
}


url = window.location.href.toString();
if(url.indexOf('question') > 0){
    removeActiveTab();
    $('#Question').addClass('active');
}else if(url.indexOf('answer') > 0) {
    removeActiveTab();
    $('#Answer').addClass('active');
}else {
    removeActiveTab();
    $('#Home').addClass('active');
}

avatar.on('click', () => {
    $('#logoutForm').submit()
});

$('#askQuestionBtn').on('click', () => {
    $('#addQuestionForm').submit()
});

$('#addQuestionBtn').on('click', () => {
    $('#addanswerForm').submit()
});
