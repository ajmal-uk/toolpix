importScripts('https://www.gstatic.com/firebasejs/8.3.2/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.3.2/firebase-messaging.js');

// Initialize Aplu
const apluPushConfig = {
    apiKey: "AIzaSyCrjPBueTXuuENlGRxBpM_pq7wge-bT1vo",
	authDomain: "aplu-a8.firebaseapp.com",
	projectId: "aplu-a8",
	storageBucket: "aplu-a8.firebasestorage.app",
	messagingSenderId: "398107472976",
	appId: "1:398107472976:web:c612a5a7bf59d1da3c4d55"
};

try {
    importScripts('https://push.aplu.io/import-aplu-messaging.js');
} catch (err) {
    console.warn("Couldn't load aplu-script, falling back: ", err);
}