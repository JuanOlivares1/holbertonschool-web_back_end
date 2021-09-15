import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const upPhoto = uploadPhoto();
  const newUser = createUser();

  try {
    return {
      photo: await upPhoto,
      user: await newUser,
    };
  } catch (e) {
    return {
      photo: null,
      user: null,
    };
  }
}
