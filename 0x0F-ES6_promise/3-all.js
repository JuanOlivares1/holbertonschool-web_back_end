import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const upPicture = uploadPhoto();
  const createUs = createUser();

  return Promise
    .all([upPicture, createUs]).then((values) => {
      console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
