import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { gsap } from 'gsap';
import './Captcha.css';  // Import your CSS file for styling

const Captcha = () => {
  const [motionDetected, setMotionDetected] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const handleDeviceMotion = (event) => {
      const { acceleration, rotationRate } = event;

      // Send motion data to the backend for verification
      axios.post('http://localhost:5000/verify-motion', {
        acceleration: event.acceleration,
        rotationRate: event.rotationRate,
      })
      .then(response => {
        setMessage(response.data.message);  // Display the result from the backend
        // Trigger success or failure animation with GSAP
        gsap.to('.captcha-message', {
          color: response.data.message.includes('human') ? '#00FF00' : '#FF0000',
          duration: 1
        });
      })
      .catch(error => {
        console.error('Error sending motion data:', error);
      });
    };

    // Listen for device motion events
    window.addEventListener('devicemotion', handleDeviceMotion);

    // Cleanup event listener on unmount
    return () => {
      window.removeEventListener('devicemotion', handleDeviceMotion);
    };
  }, []);

  return (
    <div className="captcha-container">
      <h1 className="title">Tilt or Shake to Verify</h1>
      <p className="instruction">Move your device slightly to pass the CAPTCHA.</p>
      <p className="captcha-message">{message}</p>
    </div>
  );
};

export default Captcha;
