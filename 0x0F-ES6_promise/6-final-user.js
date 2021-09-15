import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUser = signUpUser(firstName, lastName);
  const uploadPicture = uploadPhoto(fileName);
  const rtnArr = [];

  return Promise
    .allSettled([signUser, uploadPicture]).then((values) => {
      for (const i of values) {
        rtnArr.push({
          status: i.status,
          value: i.value !== undefined ? i.value : `${i.reason.name}: ${i.reason.message}`,
        });
      }
      return rtnArr;
    });
}
