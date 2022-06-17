
--* RestoreFromTempTable
CREATE TABLE m_memo (
  id serial NOT NULL
  , content text
  , create_user_id character varying(13) NOT NULL
  , created_at timestamp(3) with time zone NOT NULL
  , update_user_id character varying(13) NOT NULL
  , updated_at timestamp(3) with time zone NOT NULL
) ;
