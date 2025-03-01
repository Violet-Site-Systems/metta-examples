import { StytchUIClient } from '@stytch/vanilla-js';

const stytch = new StytchUIClient('public-token-test-228f061e-d81e-4062-9e54-6991ae874de6');

export const mountIDP = () => {
  const styles = { fontFamily: 'Arial' };

  stytch.mountIDP({
    // replace this with a selector for the element where you want to render the component
    elementId: '#stytch-idp-container',
    styles,
  });
};
